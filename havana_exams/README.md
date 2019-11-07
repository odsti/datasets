# Mathematics exam marks for Havana pre-university students

Inspired by [Resultados del examen de ingreso de Matemática en La
Habana](https://proyectoinventario.org/resultados-examen-ingreso-matematica-habana).

> Las cifras siguientes se basan en la [Relación de notas por preuniversitarios]
> (http://www.uh.cu/sites/default/files/public/adjuntos/matematica_notas_ordinaria.pdf)
> emitida el 9 de mayo por la Comisión de Ingreso Provincial de La Habana,
> y divulgada por el sitio web de la Universidad de La Habana.

* `matematica_notas_ordinaria.pdf` is the PDF from the link above, and
  therefore, the 2019 results for mathematics.  Results released 9th May 2019.

Exploration of <http://www.uh.cu> with [wget
-r](https://www.gnu.org/software/wget) led me to the [2018 examination results
page](http://www.uh.cu/noticia/resultados-de-los-examenes-de-ingreso-la-universidad),
and to the results for:

* [Mathematics in
  2018](http://www.uh.cu/sites/default/files/public/adjuntos/notas_de_matematica_ordinaria.pdf);
  filename `notas_de_matematica_ordinaria.pdf`, released 10 May 2018.
* [Spanish in
  2018](http://www.uh.cu/sites/default/files/public/adjuntos/notas_de_espanol_ordinaria.pdf);
  filename `notas_de_espanol_ordinaria.pdf`, released 17 May 2018.
* [History in
  2018](http://www.uh.cu/sites/default/files/public/adjuntos/notas_de_historia_ordinaria.pdf);
  filename `notas_de_historia_ordinaria.pdf`, released 17 May 2018.

* `matematica_notas_ordinaria.html` is the HTML resulting from conversion of
  the 2019 PDF with <https://www.pdftohtml.net>.  Likewise, each PDF listed
  above has a matching `.html` file converted at that site.
* `scrape_havana_exams.py` scrapes the HTML files to generate the Pandas data
  frame.
* `processed/havana_*.csv` are the data files output from the script.

See the page linked at the top for more analysis of the 2019 data.
`scrape_havana_exams.py` does some checks that our results look the same as
theirs.

Data dictionary for `processed/havana_*.csv` files:

* `school`: candidate's school ("Preuniversitario" in the original).
* `school_type`: category of the school ("Vía de ingreso" in the original).
* `id`: identity card number (unique for every resident of Cuba).
* `name`: "Apellidos y nombre(s)" in the original. Following the Spanish
  convention, the first two names are surnames ("apellidos").
* `mark`: mark in the exam, with `NaN` if they candidate did not show up for
  the exam.

I assume these data are public, therefore
[CC0](https://creativecommons.org/choose/zero).  I (MB) release the code as
CC0 also.
