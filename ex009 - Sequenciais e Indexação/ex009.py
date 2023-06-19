#Sequencias

#Lista em colchetes [] <- Essa é uma lista vazia.
listaVazia = []

print(listaVazia)

#Lista em colchetes, separado os itens por vírgulas.
lista = [101,202,303,404,505]
print(f"lista = {lista}")
print(f"lista = {lista[0]}")
print(f"lista = {lista[1]}")
print(f"lista = {lista[2]}")
print(f"lista = {lista[3]}")
print(f"lista = {lista[4]}")

#Lista em colchetes, usando a compreensão de lista.
lista = [101 for list in iterable]
#Lista usando o construtor do tipo list
list(iterable)
print(list)

"""Lembrando que assim como em C e em Java, o Python trabalha com a indexaçãodos itens que se inicia com 0 e cada itemtem o seu índice incrementado uma unicade em relação ao seu item anterior. Python tbm permite indexação com números negativos. O valor -1 é o indice do ultimo item, e cada item anterior é decrementado de uma unidade em relação ao sucessor."""

lista = ["Matheus", "Giulia", "Ismael", "Timóteo", "Evangeline", "Amanda"]
sobrenome = ("Urban")
print(lista[-1] + " " + sobrenome)

'''Como podemos ver, tbm podemos usar o valor negativo, como sa foi explicado.'''