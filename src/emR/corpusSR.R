#Formacao Cientista de Dados - Fernando Amaral

#############
# Instalar o pacot4e tm (text miner)
#############
install.packages("C:/Users/jailton/Downloads/tm_0.7-7/tm/R/tm")
install.packages("tm", repos="http://cran.us.r-project.org")
install.packages("wordcloud")

getSources()
getReaders()

#corpus = VCorpus(DirSource("E:/Minera??o de dados/Textmining/texto", encoding = "UTF-8"),readerControl = list(reader=readPlain,language = "por"))
# Lê o corpo de daos em memória (VCorpus)
corpusSR = VCorpus(DirSource("C:/UFPE/20192/SystematicReview/ResultSelected", encoding = "", ignore.case = FALSE),readerControl = list(reader=readPDF,language = "eng"))
# carrega todos os arquivos (1000)

inspect(corpusSR) 
inspect(corpus[1:100])
#Ler os 100 primeiros

# Mostra os metadados do corpus
meta(corpusSR[[1]])  

# Mostra o corpus
inspect(corpusSR[[2]])  

as.character(corpusSR[[2]]) 
as.character(corpusSR[[2]])[1] 

# Retorna lista de palavras sem valor semantico
stopwords("portuguese")
stopwords("english")

# Remove stopwords
corpusSR = tm_map(corpusSR, removeWords, stopwords("english"))
corpusSR = tm_map(corpusSR, removeWords, 
                  c(stopwords("english"),"the","The","can","will","this","use"
                             ,"new","one","for","may","\024\005\b","fig"
                             ,"figure","also","ieee","author","allow"
                             ,"key","generat","differ","includ")) 

# remosver os excessos de espacos em branco
corpusSR = tm_map(corpusSR , stripWhitespace)

# Remover pontuacao
corpusSR  <- tm_map(corpusSR , removePunctuation)

# Remover numeros
corpusSR  <- tm_map(corpusSR , removeNumbers)

# Ver outras funcooes tm_map

corpusSR = tm_map(corpusSR, stemDocument,language = "english")
corpusSR = tm_map(corpusSR, stemCompletion, dictionary=corpusSR)

library(wordcloud)
wordcloud(corpusSR,max.words=40,random.order=T,colors=rainbow(8),rot.per=0.8,use.r.layout=T)

# Usando termDocumentMatrix

freq <- TermDocumentMatrix(corpusSR)
matriz <- as.matrix(freq)
matriz <- sort(rowSums(matriz),decreasing=TRUE)
matriz = data.frame(word=names(matriz), freq=matriz)
head(matriz, n=500)

wordcloud(matriz,max.words=100,random.order=T,colors=rainbow(8),rot.per=0.5,use.r.layout=T)

findFreqTerms(freq,1000,Inf)

removeSparseTerms(freq, 0.4)
