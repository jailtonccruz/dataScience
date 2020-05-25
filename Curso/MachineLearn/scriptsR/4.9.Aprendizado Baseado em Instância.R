#Formacao Cientista de Dados - Fernando Amaral

install.packages("class", dependencies=T)
library(class)

dim(iris)
head(iris)
summary(iris)

# Dividir a amostra em 2 
amostra = sample(2,150,replace=T, prob=c(0.7,0.3))

iristreino = iris[amostra==1,]
classificar = iris[amostra==2,]

dim(iristreino)
dim(classificar)

# Buscar o vizinho mais próximo
# Iristreino é onde vai buscar o vizinho mais próximo
# Classificar dados que vai classificar
# iristreino[,5] Onde estao as classes
previsao = knn(iristreino[,1:4],classificar[,1:4],iristreino[,5],k=3)

previsao

# matriz de confusao
tabela = table(classificar[,5],previsao)

(tabela[1] + tabela[5] + tabela[9]) / sum(tabela) 


