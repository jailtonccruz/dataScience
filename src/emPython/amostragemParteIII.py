# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 01:38:49 2020

@author: jailton
"""
import numpy as np

import pandas as pd

# ceil - funcao para arredondamento
from math import ceil

# Então temps umapopulacao de 150 na qual queremos seleconar apenas 15
populacao = 150
amostra = 15

k= ceil(populacao / amostra)

k

r = np.random.randint(low = 1, high = k + 1, size = 1)

acumulador = r[0]
sorteados = []
for i in range(amostra):
    #print(acumulador)
    sorteados.append(acumulador)
    acumulador += k
    
base = pd.read_csv('C:\dataScience\RdataSets\iris.csv')
base_final = base.loc[sorteados]
    






