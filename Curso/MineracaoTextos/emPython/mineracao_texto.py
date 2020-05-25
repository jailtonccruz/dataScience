####################################
## Mineracao de textos
####################################
import matplotlib.pyplot as plt
import nltk
#nltk.download()
from nltk.corpus import PlaintextCorpusReader

# from nltk.corpus import 
from nltk.corpus import stopwords
from matplotlib.colors import ListedColormap
from wordcloud import WordCloud
import string




#corpus = PlaintextCorpusReader('C:\dataScience\Curso\MineracaoTextos\Dados', '.*')
corpus = PlaintextCorpusReader('C:\UFPE\20192\SystematicReview\ResultSelected', '.*')

arquivos = corpus.fileids()
arquivos[0]
arquivos[0:100]
for a in arquivos:
    print(a)
    
texto = corpus.raw('1.txt')

todo_texto = corpus.raw()
palavras = corpus.words()
palavras[150]
len(palavras)

stops = stopwords.words('english')
mapa_cores = ListedColormap(['orange', 'green', 'red', 'magenta'])
nuvem = WordCloud(background_color = 'white',
                  colormap = mapa_cores,
                  stopwords = stops,
                  max_words = 50)
nuvem.generate(todo_texto)
plt.imshow(nuvem)

palavras_semstop = [p for p in palavras if p not in stops]
len(palavras_semstop)

palavras_sem_pontuacao = [p for p in palavras_semstop if p not in string.punctuation]
len(palavras_sem_pontuacao)

frequencia = nltk.FreqDist(palavras_sem_pontuacao)
mais_comuns = frequencia.most_common(100)

