# Mathematics exam marks for Havana pre-university students

From [Resultados del examen de ingreso de Matemática en La
Habana](https://proyectoinventario.org/resultados-examen-ingreso-matematica-habana).

> Las cifras siguientes se basan en la [Relación de notas por preuniversitarios]
> (http://www.uh.cu/sites/default/files/public/adjuntos/matematica_notas_ordinaria.pdf)
> emitida el 9 de mayo por la Comisión de Ingreso Provincial de La Habana,
> y divulgada por el sitio web de la Universidad de La Habana.

* `matematica_notas_ordinaria.pdf` is the PDF from the link above.
* `matematica_notas_ordinaria.html` is the HTML resulting from conversion of
  this PDF with <https://www.pdftohtml.net>.
* `scrape_havana_math.py` scrapes the HTML file to generate the Pandas data frame.
* `processed/havana_math.csv` is data output from the script.

See the page linked at the top for more analysis.  `scrape_havana_math.py` does
some checks that our results look the same as theirs.

Data dictionary for `processed/havana_math.csv`:

* `school`: candidate's school ("Preuniversitario" in the original).
* `school_type`: category of the school ("Vía de ingreso" in the original).
* `id`: identity card number (unique for every resident of Cuba).
* `name`: "Apellidos y nombre(s)" in the original. Following the Spanish
  convention, the first two names are surnames ("apellidos").
* `mark`: mark in the exam, with `NaN` if they candidate did not show up for
  the exam.

I assume these data are public, therefore
[CC0](https://creativecommons.org/choose/zero).  I (MB) release the code as CC0
also.
