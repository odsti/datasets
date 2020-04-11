""" Utilities for working with datasets
"""

import os.path as op

from download import download_with_resume


def get_original(url, fname, hash=None, timeout=10):
    out_fname = op.join('originals', fname)
    download_with_resume(url, out_fname, hash, timeout)
    return out_fname
