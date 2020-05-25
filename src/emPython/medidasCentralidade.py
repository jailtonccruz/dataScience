# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 16:41:49 2020

@author: jailton
"""

import numpy as np
#from scipy import stats    
import scipy as sy

amostra1 = [62, 58, 70, 65, 80]
amostra2 = [63, 63, 63, 63, 63]
amostra3 = [42, 65, 55, 78, 75]
amostra4 = [68, 46, 85, 90, 56]

np.mean(amostra1)
np.median(amostra1)
quartis = np.quantile(amostra1, [0, 0.5, 1])
quartis
np.average(amostra1)


np.std(amostra1)

# Distribuicao binomial
from scipy.stats import binom
#

probCara = binom.pmf(3,5,0.5)
print(probCara)

# prova 12 questoes
# probabilidade de acertar 7 questoes
# cada questao 4 alternativas
probProva = binom.pmf(7, 12, 0.25)
print(probProva)

# 4 sinais de 4 tempos
# probabilidade de sinal ta verde 0,1,2,3,4 0,25

probVerde1 = binom.pmf(1,4,0.25) # prop.de encontra 1 verde
print(probVerde1)
probVerde2 = binom.pmf(2,4,0.25) # prop.de encontra 2 verdes
print(probVerde2)
probVerde3 = binom.pmf(3,4,0.25) # prop.de encontra 3 verdes
print(probVerde3)
probVerde4 = binom.pmf(4,4,0.25) # prop.de encontra 4 verdes 
print(probVerde4)

# probabildade cumulativa

probCum = binom.cdf(4,4,0.25) # prop.de encontra 1 verde
print(probCum)

# Distribuicao normal
from scipy.stats import norm

# Seja media = 8, dp = 2, objeto < 6
# obs: usa cdf quando menor e sf quando maior
aleat = norm.cdf(6,8,2)
print(aleat)


# Seja media = 8, dp = 2, objeto > 6
aleat = norm.sf(6, 8, 2)
print (aleat)


# Seja media = 8, dp = 2, peso objeto > 6 ou menor que 10
aleat = norm.cdf(6,8,2) + norm.sf(10, 8, 2)
print(aleat)

# Seja media = 8, dp = 2, peso objeto menor que 10 e menor que 8
aleat = norm.cdf(10,8,2) - norm.cdf(8,8,2)
print(aleat)

# teste para saber se a distribuicao e normal
from scipy import stats
from scipy.stats import norm
import matplotlib.pyplot as plt

# pyplot recursos graficos do pyton

# gerar os dados
dados = norm.rvs(size = 100)
stats.probplot(dados, plot= plt)

stats.shapiro(dados)

####
#T de Student
####

# media salario 75 Dp 10 amosra 9
# Qual a probabilidade de selecionar um cientista
#  de dados que ganhe salario MENOR que 80
# t = 1,5

from scipy.stats import t

tstMenor = t.cdf(1.5, 8)
print(tst)


# selecionar um cientista
#  de dados que ganhe salario MAIOR que 80
tstMaior = t.sf(1.5, 8)
print(tstMaior)














