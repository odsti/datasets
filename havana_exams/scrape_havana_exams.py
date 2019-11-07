""" Scrape HTML output from PDF with mathematics marks
"""
import os.path as op

import numpy as np
import pandas as pd

from bs4 import BeautifulSoup

COLUMNS = ('school', 'school_type', 'id', 'name', 'mark')

# From: https://proyectoinventario.org/resultados-examen-ingreso-matematica-habana
# The page gives this list of Vía de ingreso.  'Colegio Universitario' added
# from the 2018 mathematics data. 'Escuelas Profesionales de Arte' added from
# the 2018 Spanish data.
VIAS = set(('Academias Deportivas de Alto Rendimiento',
            'Cadetes MININT',
            'Colegio Universitario',
            'Escuelas Profesionales de Arte',
            'Concurso',
            'Escuelas de Iniciación Deportiva',
            'Institutos Preuniversitarios',
            'ORDEN 18',
            'Servicio Militar Voluntario Femenino examina'))


def read_pages(html_fname):
    # Read the HTML into memory.
    with open(html_fname, 'rt') as fobj:
        html_doc = fobj.read()

    # Parse HTML into objects.
    soup = BeautifulSoup(html_doc, 'html.parser')

    # All marks and relevant text are in <div> tags.
    return [c for c in soup.body.children if c.name == 'div']


def process_page(page):
    """ Parse page data into list of student entries.

    One student entry is a list with values corresponding to:

    * school
    * school_type
    * id
    * name
    * mark (float)
    """
    divs = [c for c in page.children if c.name == 'div']
    entries = [e.text for e in divs if 'cls_007' in e.attrs.get('class', [])]
    school, via = entries[0:2]
    s_entries = entries[2:]
    assert len(s_entries) % 3 == 0
    assert len(s_entries) >= 3
    students = []
    for i in range(0, len(s_entries), 3):
        id_no, name, mark = s_entries[i:i+3]
        # Marks have , for decimal separator.
        # Aus means "Ausente" - absent.  Replace with NaN.
        # Des means - what?
        mark = (np.nan if mark in ('Aus', 'Des')
                else float(mark.replace(',', '.')))
        students.append([school, via, id_no, name, mark])
    return students


def process_pages(pages):
    # Concatenate the list from each page into one list.
    return sum([process_page(p) for p in pages], [])


def import_html(html_fname, n_pages):
    pages = read_pages(html_fname)
    assert len(pages) == n_pages
    students = process_pages(pages)
    df = pd.DataFrame(students, columns=COLUMNS)
    assert VIAS.issuperset(df['school_type'])
    return df


# 2019 analysis.
# Check found number of pages against last page number in the 2019 PDF.
n_pages_2019 = 307
df_2019 = import_html('matematica_notas_ordinaria.html', n_pages_2019)

# From: https://proyectoinventario.org/resultados-examen-ingreso-matematica-habana
#
# De los 7 735 estudiantes que debían tomar el examen, no se presentaron 775,
# para un total de 6 960 examinados que sí recibieron una nota.
assert len(df_2019) == 7735
assert np.sum(df_2019['mark'].isna()) == 775

# Save to CSV without row labels
df_2019.to_csv(op.join('processed', 'havana_math_2019.csv'), index=False)

# 2018 mathematics.
n_pages_2018 = 319
df_2018 = import_html('notas_de_matematica_ordinaria.html', n_pages_2018)

# Save to CSV without row labels
df_2018.to_csv(op.join('processed', 'havana_math_2018.csv'), index=False)

# 2018 Spanish.
n_esp_2018 = 321
df_esp_2018 = import_html('notas_de_espanol_ordinaria.html', n_esp_2018)

# Save to CSV without row labels
df_esp_2018.to_csv(op.join('processed', 'havana_spanish_2018.csv'), index=False)

# 2018 Cuban History.
n_hist_2018 = 321
df_hist_2018 = import_html('notas_de_historia_ordinaria.html', n_hist_2018)

# Save to CSV without row labels
df_hist_2018.to_csv(op.join('processed', 'havana_history_2018.csv'), index=False)
