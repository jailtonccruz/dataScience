install.packages("e1071", dependences=T)
library(e1071)
credito = read.csv(file.choose(), sep=",", header=T)
#Checar o arquivo
head(credito)
#Estrutura do dataset
dim(credito)
#Gerar aa  base se teste e de treino
amostra = sample(2, 1000, replace=T, prob = c(0.7, 0.3))
amostra

#Gerar a base de treinamento
creditotreino = credito[amostra==1,]
creditotreino

#Gerar a base de testes
creditoteste = credito[amostra==2,]
creditoteste

dim(creditotreino)
dim(creditoteste)

# Criacao do mmodelo
modelo = naiveBayes(class ~. , creditotreino)
modelo
class(modelo)

#Testando o modelo
predicao = predict(modelo, creditoteste)
predicao

#Matriz de confusao
confusao = table(creditoteste$class, predicao)
confusao

# Calcular a taxa de acerto
taxaacerto = (confusao[1] + confusao[4]) / sum(confusao)

# Analisando um no9vo pedido de credito
novocredito = read.csv(file.choose(), sep=",", header=T)
novocredito
dim(novocredito)

novapredicao = predict(modelo, novocredito)
novapredicao
