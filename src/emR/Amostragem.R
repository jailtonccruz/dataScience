# Data Science em R
iris

# Dimensao
dim(iris)
#Funcoes de amostragem
# Gera amostragens aleatorias

# R: Amostragem parte I

# Ex.1
amostra = sample(c(0,1), 150, replace = TRUE, prob=c(0.4, 0.6))
amostra
length(amostra[amostra==1])
# Fun?a? set.seed cria a semente de aleatoriedade
set.seed(2345)
#Fun??o para gerar amostras aleat?rios
V1 = sample(c(100),1)
V1
#
#Fun??o strata
#
amostrairis2 = strata(iris,c("Species"),size=c(25,25,25),method="srswor")
amostrairis2
dim(amostrairis2)
summary(amostrairis2)

S.SY()

# R: Amostragem parte II

# Instalandoo pacote
install.packages("sampling")

# Carregando o pacote
library(sampling)

# Conjunto de dados inferty
infert

# Sumario do data set
summary(infert)

# Gerando um conjunto de dados com tamanho x a partir de outro dataset
# divide o dataset proporciolnal ao numero de elemento de cada estrato
# se o tamanho e X, num.elem / amostraTotal * x 
# Seja X = 100, education 6-11: 120 amostra total 248
tamNovaAmostra= 120 / 248 * 100
tamNovaAmostra

novaAmostra = strata(infert, c("education"), size = c(5,48,47), method = "srswor")
novaAmostra
dim(novaAmostra)
summary(novaAmostra)

# R: Amostragem parte III
# Amostrage sistematica


install.packages("TeachingSampling")

# Carregando o pacote
library(TeachingSampling)

# gerando uma amostra sistematica no dataset iris
# Funcao S.SY
amostraSist = S.SY(150,10)

amostraSist


  amostraSistIris = iris(amostraSist,)
  
# Medidas de variabilidade e centralidade
amostra1 = c(62, 58, 70, 65, 80)
mean(amostra1)
median(amostra1)
quartis1 = quantile(amostra1)
quartis1
sd(amostra1)
summary(amostra1)
var(amostra1)


amostra2 = c(63, 63, 63, 63, 63)
mean(amostra2)
median(amostra2)
quartis2 = quantile(amostra2)
quartis2
sd(amostra2)
var(amostra2)

amostra3 = c(42, 65, 55, 78, 75)
mean(amostra3)
median(amostra3)
quartis3 = quantile(amostra3)
quartis3
sd(amostra3)
var(amostra3)

amostra4 = c(68, 46, 85, 90, 56, 130)
mean(amostra4)
median(amostra4)
quartis4 = quantile(amostra4)
quartis4
sd(amostra4)
var(amostra4)

