# R script to write Mardia 1979 data
if (!('bnlearn' %in% installed.packages()[,"Package"])) {
    install.packages('bnlearn')
}
library(bnlearn)
data(marks)
out_path <- file.path('processed', 'mardia_marks.csv')
write.csv(marks, out_path, row.names=FALSE)
