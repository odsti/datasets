# Data from:
# Galton, F. (1886). Regression Towards Mediocrity in Hereditary Stature
# Journal of the Anthropological Institute, 15, 246-263

install.packages('HistData')
library(HistData)
data(Galton)
write.csv(Galton, 'processed/galton_heights.csv', row.names=FALSE)
write.csv(GaltonFamilies, 'processed/galton_combined.csv', row.names=FALSE)
