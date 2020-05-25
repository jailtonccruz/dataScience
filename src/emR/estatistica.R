# Distribuicao binomial

x = 0
x
for (i in 1:10000)
{
  y = sample(1:6,1)
  y
  x = x + y
}
x = x / 10000
x

# Jogar uma moeda 5 vezes, qual a 
# probabilidade de dar cara 3 vezes

d = dbinom(3,5,0.5)
d

# prova 12 questoes
# probabilidade de acertar 7 questoes
# cada questao 4 alternativas
dbinom(7, 12, 0.25)

# 4 sinais de 4 tempos
# probabilidade de sinal ta verde 0,1,2,3,4 0,25

dbinom(1,4,0.25) # prob.de encontrar 1 verde
dbinom(2,4,0.25) # prob.de encontrar 2 verdes
dbinom(3,4,0.25) # prob.de encontrar 2 verdes
dbinom(4,4,0.25) # prob.de encontrar 2 verdes
# probabildade cumulativa
pbinom(4,4,0.25) # prob.de encontra 1 verde

######################################
# Distribuicao normal parte I
######################################

# Funcoes
# rnorm()  - funcao para gerar numeros aleatorios
# qqnorm() - teste de normalidade
# qqline()- gera a linah do grafico qqnorm
# shapiro.test() - executa o teste de shapiro wilk

# Seja media = 8, dp = 2, objeto < 6
pnorm(6,8,2)

# Seja media = 8, dp = 2, objeto > 6
pnorm(6,8,2,lower.tail = F)

# ou
1 - pnorm(6,8,2)

# menos de 6k ou maisde 10k
pnorm(6,8,2) + pnorm(10,8,2, lower.tail = F)

# menor que 10 e maior que 8
pnorm(10,8,2) - pnorm(8,8,2, lower.tail = F)

#Gerar um diagrama de normalidade
# gerar numeros aleatorios
aleat = rnorm(100)
aleat

# Gerar o grafico
qqnorm(aleat)

# Gerar a linha 
qqline(aleat)

# shapito teste
shapiro.test(aleat)

####
#T de Student
####

# media salario 75 Dp 10 amosra 9
# Qual a probabilidade de selecionar um cientista
#  de dados que ganhe salario menor que 80
# t = 1,5
pt(1.5, 8)

pt(1.5, 8, lower.tail = F)

####################
## Regressao linear simples
####################
dim(cars)

head(cars)
cor(cars)

# Criar um modelo usando a funcao lm (linear model)
modelo = lm(speed ~ dist, data=cars)
modelo
plot(modelo)
abline(modelo)
modelo$coefficients
modelo$coefficients[1]
modelo$coefficients[2]

# previsao
#Inercepcao + distencia * o valor q quero prever
modelo$coefficients[1] + modelo$coefficients[2] * 22
predict(modelo, data.frame (dist = 22))

summary(modelo)
#outras informacoes do modelo
modelo$fitted.values
modelo$residuals
modelo$coefficients

# Regressao linear Multipla

colnames(mtcars)
dim(mtcars) #32 registros(veiculos) e 11 colunas(caracteristicas)
cor(mtcars)
cor(mtcars[1:4]) #Buscar correlacao entre mpg e disp
# -0.8475514 correlacao negativa (correlacao forte >.7)
# valor negativo: enquanto uma variavel cresce outra decresce
# mas mantendo a correlacao
# Crriar o modele. Usa a Funcao lm

modelCars = lm(mpg ~ disp, data=mtcars) 
# mpg milha por galao Miles/(US) gallon
# cilcindrada         Displacement (cu.in.)
# Coeficiente de determinacao 

r2 = summary(modelCars)$r.squared
r2
r2Adj = summary(modelCars)$adj.r.squared
r2Adj
# Obs: r2Adj sempre menor que r2
plot(mpg ~ disp, data=mtcars)
# Quanto menor a cilindrada, maior o consumo
#Linha de melhor ajuste
abline(modelCars)
#Linha sobe para esquerda, correlacao negativa

# fazer previsoes
predict(modelCars, data.frame(disp=200))
# Para disp = 200 o consumo seria 21 galoes

#
# Modelo de regressao linear multipla
#
ModelCarsRLM = lm(mpg ~ disp + hp + cyl, data=mtcars) 
# hp - cavalos, cyl - num. de cilindros
ModelCarsRLM

summary(ModelCarsRLM)$r.squared
summary(ModelCarsRLM)$adj.r.squared
predict(ModelCarsRLM, data.frame(disp= 200, hp = 100, cyl = 4))
plot(ModelCarsRLM)

#########################################
# Regressao linear logistica
#########################################

eleicao = read.csv(file.choose(), sep=";", header="T")
fix(eleicao)
plot(eleicao$DESPESAS, eleicao$SITUACAO)
cor(eleicao$DESPESAS, eleicao$SITUACAO)

modelo = glm(SITUACAO ~ DESPESAS, data=eleicao, family = "binomial")
# General Linear Model
# bonomial -> regressao logistica

plot(eleicao$DESPESAS, eleicao$SITUACAO, col = 'read', phc = 20)

# gerar pontos q são ajustes feitos pelo modelo
points(eleicao$DESPESAS, modelo$fitted, pch = 4)

# Prever novos candidatos
preverEleicao = read.csv(file.choose(), sep=";", header="T")
fix(preverEleicao)

prevereleicao$RESULT = predict(modelo, newdata = preverEleicao, type = "response")
prevereleicao$RESULT
fix(prevereleicao$RESULT)







