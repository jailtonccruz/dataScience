# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 16:19:20 2020

@author: jailton
"""

####################
## Regressao linear simles
####################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from yellowbrick.regressor import ResidualsPlot

import statsmodels.formula.api as sm

base = pd.read_csv('C:\dataScience\RdataSets\cars.csv')
base
base = base.drop(['Unnamed: 0'], axis = 1)
base

x = base.iloc[:, 1].values
x
y = base.iloc[:, 0].values
y

correl = np.corrcoef(x, y)

modelo = LinearRegression()


# fazer reshape
x = base.iloc[:, 1].values
x = x.reshape(-1, 1)
modelo = LinearRegression()
modelo.fit(x, y)

modelo.intercept_
modelo.coef_

plt.scatter(x,y)

# tracar  a linha da regressao
plt.plot(x, modelo.predict(x), color = 'red')

# fazer a previsao
modelo.intercept_ + modelo.coef_ * 22

modelo.predict(22)

# Ver biblioteca wellbrickick: machine learn visualization
# Residual
modelo._residues

visualizador = ResidualsPlot(modelo)
visualizador.fit(x,y)
visualizador.poof()

#
# Regresao Linear multipla
#

base = pd.read_csv('C:\dataScience\RdataSets\mtcars.csv')
base
base = base.drop(['Unnamed: 0'], axis = 1)
base

# relacaao entre o consumo e a cilindrada

vInd = base.iloc[:, 2].values
vInd
vDep = base.iloc[:, 0].values
vDep
correl = np.corrcoef(vInd, vDep)
correl
# Correlacao negativa forte -> enquanto vInd aumenta vDep diminui
vInd = vInd.reshape(-1, 1)
vInd

modLinReg = LinearRegression()
modLinReg.fit(vInd, vDep)
modLinReg.intercept_
modLinReg.coef_
modLinReg.score(vInd, vDep)

# Previsao

modelPrev = modLinReg.predict(vInd)
modelPrev

# para tornar os comandos parecidos com o R
modelAdjust = sm.ols(formula = 'mpg ~ disp', data  = base)

modelTrein  = modelAdjust.fit()
modelTrein.summary()
# Mostrar o grafico

plt.scatter(vInd, vDep)
plt.plot(vInd, modelPrev, color = 'red')

modLinReg.predict(200)

modelAdjust.predict(200)

##############################
### Regressaoo linear multipla
##############################

base = pd.read_csv('C:\dataScience\RdataSets\mtcars.csv')
base
base = base.drop(['Unnamed: 0'], axis = 1)
base

x1 = base.iloc[:, 1:4].values

y1 = base.iloc[:, 0].values

modelMultLR = LinearRegression()
modelMultLRTrein = modelMultLR.fit(x1, y1)

modelMultLRTrein.score(x1, y1)

modelAdjust2 = sm.ols(formula = 'mpg ~ cyl + disp + hp', data  = base)
modelTrein2  = modelAdjust.fit()
modelTrein2.summary()

novo = np.array([4, 200, 100])
novo = novo.reshape(1, -1)

modelMultLR.predict(novo)

#########################################
# Regressao linear logistica
#########################################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


from sklearn.linear_model import LogisticRegression

base = pd.read.csv("eleicao.csv", sep = ';')
plt.scatter(base.DESPESAS, base.SITUACAO)
base.describe()

np.corrcoef(base.DESPESAS, base.SITUACAO)

X = base.iloc[:, 2].values
X = X[:, np.newaxis]
y = base.iloc[:, 1].values

modelo = LogisticRegression()
modelo.fit(X, y)
modelo.coef_
modelo.intercept_

plt.scatter(X,y)
X_teste = np.linspace(10,300,100)

def model(x):
    return 1 / 1 + (np.exp(-x))

r = model(X_teste * modelo.coef_ + model.intercept_).ravel()
plt.plot(X_teste, r, color = 'red')

base_previsoes = pd.read_csv('novosCandidatos.csv' , sep = ';')
despesas = base_previsoes.iloc[:, 1].values

despesas = despesas.reshape[-1, 1]    
previsoes_teste = modelo.predict(despesas)
base_previsoes = sp.column_stack((base_previsoes, previsoes_teste))

    






