import numpy as np
from scipy.stats import chi2_contingency


novela = np.array([[19, 6], [43, 32]])

chi2_contingency(novela)

# Importante he o valor de p, maior que 0,15 (alfa 0,015)
# não podemos rejeitar a hipotese nula