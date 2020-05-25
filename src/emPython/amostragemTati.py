# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 18:07:33 2020

@author: jailton
"""
import numpy as np

import pandas as pd

from sklearn.model_selection import train_test_split

# carregar os dados do arquivo
iris = pd.read_csv('C:\dataScience\RdataSets\iris.csv')

iris

# realizar a contagem de cada classe do arquivo
iris['Species'].value_counts()
print(iris['Species'].value_counts())

# gerar amostragem de 50% de todos os dados
# iloc seleciona partes específicas da base de dados
X, _, Y, _ = train_test_split(iris.iloc[:, 1:5], iris.iloc[:, 5], test_size=0.5,
                             stratify=iris.iloc[:, 5])

print(Y.value_counts())


# experimento com a base de dados infert

infert = pd.read_csv('C:\dataScience\RdataSets\infert.csv')
infert
print(infert['education'].value_counts())

# o _ serve para que a outra parte da divisão dos dados não sejam carregadas

X1, _, Y1, _ = train_test_split(infert.iloc[:, 2:9], infert.iloc[:, 1], test_size=0.61,
                                stratify=infert.iloc[:, 1])

print(Y1.value_counts(0))