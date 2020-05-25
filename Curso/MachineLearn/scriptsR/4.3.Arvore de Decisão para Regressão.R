#Formacao Cientista de Dados - Fernando Amaral
install.packages("e1071", dependences=T)

#modelo = rpart(Sepal.Length ~ Sepal.Width + Petal.Length +  Petal.Width + Species ,data=iris)
modelo = rpart(Sepal.Length ~ Sepal.Width + Petal.Length +  Petal.Width + Species ,data=iris)
modelo

predicao = predict(modelo, iris)
head(predicao)

comparacao = cbind(predicao,iris$Sepal.Length,predicao - iris$Sepal.Length )
head(comparacao)
x = available.packages()
x
install.packages("installr")
  updateR()
  

