# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 16:04:34 2020

@author: jailton
"""

x =1 
y = False

print(y)
print (x)

print("informe o valor")
i= input()
print(i)

# Estrutura de decisao

print("Informe a nota1")
nota1 = int(input())
print("Nota1",nota1)
print("Informe a nota 2")
nota2 = int(input())
print(nota2)
media = (nota1 + nota2) / 2
print(media)
if media < 4:
    print("Reprovado")
elif media >= 4 and media < 7:
    print("Fazer final")
else:
    print("Aprovado")

# Estrutura de repeticao

# Estrutura While (teste no inicio)

count = 0
while count < 5:
    count += 1  # count = count + 1
    print(count)

# Estrutura for (numero fixo de interacoes)
    
for n in range (0,10):
    print(n)

# Listas
    
list1 = [1,2,3,7]
print(len(list1))
print(list1[2])
list2 = [2,4,6,list(range(0,10))]
print(list2)
print(list2[3])

for n in range (0, len(list2)):
    print(list2[n])

# Modulos e pacotes
    
import statistics as stat
x = stat.mean(z)

y = stat.median(z)

print(x)
    




