#Formacao Cientista de Dados - Fernando Amaral
boxplot(iris[,1:4])

iris_padr = boxplot( scale(iris[,1:4]))
boxplot(iris_padr)


normaliza = function(x){
  return((x-min(x))/(max(x)-min(x)))
}

iris_norm = normaliza(iris[,1:4])
boxplot(iris_norm)