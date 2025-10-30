
#1 Dobro dos números (map + lambda)
#Dada a lista [1, 2, 3, 4, 5], use map com lambda para gerar uma nova lista com o dobro de cada número.

numeros = [1, 2, 3, 4, 5]
dobrados = list(map(lambda x: x * 2, numeros))
print(dobrados)


 #2 Dada a lista [10, 15, 20, 25, 30], use filter com lambda para obter apenas os números pares.
numeros = [10, 15, 20, 25, 30]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Números pares:", pares)


#3 Soma dos números (reduce + lambda)
#Usando reduce, some todos os números da lista [1, 2, 3, 4, 5].

from functools import reduce
numeros = [1, 2, 3, 4, 5]
soma = reduce(lambda x, y: x + y, numeros)
print(soma)


#4 Ordenação por comprimento da palavra (sorted + lambda)

#Dada a lista ["uva", "banana", "maçã", "laranja"], ordene as palavras pelo tamanho usando sorted e lambda.

palavras = ["uva", "banana", "maçã", "laranja"]
ordenadas = sorted(palavras, key=lambda x: len(x))
print(ordenadas)


#5 primeira letra maiúscula (map + lambda)
#Dada a lista ["ana", "pedro", "maria"], use map e lambda para transformar em ["Ana", "Pedro", "Maria"].

nomes = ["ana", "pedro", "maria"]
capitalizados = list(map(lambda nome: nome.capitalize(), nomes))
print(capitalizados)


#6 Produto dos números (reduce + lambda)

#Usando reduce, calcule o produto (multiplicação) de todos os elementos da lista [2, 3, 4, 5].
from functools import reduce

numeros = [2, 3, 4, 5]
produto = reduce(lambda x, y: x * y, numeros)
print(produto) 


#6 Ordenar por último caractere (sorted + lambda)
#Dada a lista ["banana", "uva", "maçã", "laranja"], ordene as palavras pelo último caractere.

frutas = ["banana", "uva", "maça", "laranja"]
ordenadas = sorted(frutas, key=lambda x: x[-1])
print(ordenadas)
