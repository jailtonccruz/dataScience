#Formacao Cientista de Dados - Fernando Amaral
#install.packagens("mltools")
#install.packagens("data.table")

tit = as.data.frame(Titanic)
labenc = data.matrix(tit[,1:3])
library(mltools)
library(data.table)

hotenco  =    one_hot(as.data.table( tit[,1:3]))


  
  