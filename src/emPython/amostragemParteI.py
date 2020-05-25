# Amostragem em Python
# Importando Pandas - Bib utilizada na area de DataScience
import pandas as pd
import numpy as np

base = pd.read_csv('C:\dataScience\RdataSets\iris.csv')

np.random.seed(2345)

amostra = np.random.choice(a = [0, 1], size = 150, 
                           replace = True, p = (0.5, 0.5))

len(amostra)

len(amostra [amostra == 1])

len(amostra [amostra == 0])

