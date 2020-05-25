#Formacao Cientista de Dados - Fernando Amaral

novela = matrix(c(19,6,43,32),nrow=2, byrow=T)

# Apresentar a matriz 
fix(novela)

rownames(novela) = c("Masculino","Feminino")

colnames(novela) = c("Assiste","NaoAssiste")
fix(novela)

chisq.test(novela)






