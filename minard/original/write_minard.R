# Historical data package
install.packages('HistData')
library(HistData)

# Collect data into workspace
data(Minard.cities)
data(Minard.troops)
data(Minard.temp)

names(Minard.cities) = c('Longditude', 'Latitude', 'City')
write.csv(Minard.cities, 'minard_cities.csv', row.names=FALSE)

names(Minard.troops) = c('Longditude', 'Latitude', 'Survivors', 'Direction', 'Group')
write.csv(Minard.troops, 'minard_troops.csv', row.names=FALSE)

names(Minard.troops) = c('Longditude', 'Temp', 'Days', 'Date')
write.csv(Minard.temp, 'minard_temp.csv', row.names=FALSE)
