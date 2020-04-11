""" Python HTTP download with resume and optional MD5 hash checking

From: https://gist.github.com/mjohnsullivan/9322154 with thanks.
"""

import os.path
import shutil
import hashlib
import logging

# Support both Python 2 and 3 urllib2 importing
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request


def validate_file(file_path, hash):
    """
    Validates a file against an MD5 hash value

    :param file_path: path to the file for hash validation
    :type file_path:  string
    :param hash:      expected hash value of the file
    :type hash:       string -- MD5 hash value
    """
    m = hashlib.md5()
    with open(file_path, 'rb') as f:
        while True:
            chunk = f.read(1000 * 1000)  # 1MB
            if not chunk:
                break
            m.update(chunk)
    return m.hexdigest() == hash


def download_with_resume(url, file_path, hash=None, timeout=10):
    """
    Performs a HTTP(S) download that can be restarted if prematurely terminated.
    The HTTP server must support byte ranges.

    :param file_path: the path to the file to write to disk
    :type file_path:  string
    :param hash: hash value for file validation
    :type hash:  string (MD5 hash value)
    :param timout: timeout for http request
    :type timeout: int
    """
    # don't download if the file exists
    if os.path.exists(file_path):
        if hash and not validate_file(file_path, hash):
            raise Exception(
                'Error validating the file against its MD5 hash')
        return
    block_size = 1000 * 1000  # 1MB
    tmp_file_path = file_path + '.part'
    first_byte = os.path.getsize(
        tmp_file_path) if os.path.exists(tmp_file_path) else 0
    logging.debug('Starting download at %.1fMB' % (first_byte / 1e6))
    file_size = -1
    try:
        file_size = int(urlopen(url).info().get('Content-Length', -1))
        logging.debug('File size is %s' % file_size)
        while first_byte < file_size:
            last_byte = first_byte + block_size \
                if first_byte + block_size < file_size \
                else file_size - 1
            logging.debug('Downloading byte range %d - %d' %
                          (first_byte, last_byte))
            # create the request and set the byte range in the header
            req = Request(url)
            req.headers['Range'] = 'bytes=%s-%s' % (first_byte, last_byte)
            data_chunk = urlopen(req, timeout=timeout).read()
            # read the data from the URL and write it to the file
            with open(tmp_file_path, 'ab') as f:
                f.write(data_chunk)
            first_byte = last_byte + 1
    except IOError as e:
        logging.debug('IO Error - %s' % e)
    finally:
        # rename the temp download file to the correct name if fully downloaded
        if file_size == os.path.getsize(tmp_file_path):
            # if there's a hash value, validate the file
            if hash and not validate_file(tmp_file_path, hash):
                raise Exception(
                    'Error validating the file against its MD5 hash')
            shutil.move(tmp_file_path, file_path)
        elif file_size == -1:
            raise Exception(
                'Error getting Content-Length from server: %s' % url)
