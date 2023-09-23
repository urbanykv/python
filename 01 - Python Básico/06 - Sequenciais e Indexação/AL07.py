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

#Lista usando o construtor do tipo list

liste = list("maca")
print(liste)

"""Lembrando que assim como em C e em Java, o Python trabalha com a indexaçãodos itens que se inicia com 0 e cada itemtem o seu índice incrementado uma unicade em relação ao seu item anterior. Python tbm permite indexação com números negativos. O valor -1 é o indice do ultimo item, e cada item anterior é decrementado de uma unidade em relação ao sucessor."""

lista = ["Matheus", "Giulia", "Ismael", "Timóteo", "Evangeline", "Amanda"]
sobrenome = ("Urban")
print(lista[-1] + " " + sobrenome)

'''Como podemos ver, tbm podemos usar o valor negativo, como sa foi explicado.'''

#Impressão de sequências

seq = [0, 1, 2, 3]
print(seq)

'''Para imprimir uma substring, por exemplo, basta utilizar os colchetes para indicar o intervalo de índices que deve ser impresso. Vale lembrar que o primeiro caractere da string é indexado com 0. Confira na imagem:'''

str = ("Hello World")

print(str[0:6])

print(str[2:5])

'''Usar [0:4] provoca a impressão dos índices 0, 1, 2 e 3, mas não do índice 4. Analogamente, usar [2:8] provoca a impressão dos índices de 2 a 7, mas não do 8.'''

'''//--------////--------////--------////--------'''

'''Também é possível imprimir a string como lida da direita para a esquerda. Para isso, deve-se utilizar [: : -1]. Esse valor -1 indica que a leitura dos caracteres será feita no sentido oposto ao tradicional. Observe:'''

print(str[::-1])
print(str[8:2:-1])


numeros = [1, 5, 6, 74, 8, 69]

numeros.append(55) # Adicionar no final do array (igual a ´push do JS).

numeros.insert(0, 556) # Bem parecido com o Splice do JavaScript, mas ele apenas adiciona.. o primeiro parâmetro é a posição e o segundo é oque será adicionado.

numeros.remove(74) # Remove qualquer Variável q for passada no parâmetro.

numeros.pop(2) # Remove usando o indice como parâmetro para remoção.

print(numeros)

# Objetos


linguagens = ["JavaScript", "Python", "C++", "Java", "Delphi", "C#", "PHP"]

# usando for

contador = 0

for linguagem in linguagens:
    contador += 1
    print(f"{contador} - {linguagem}")
else:
    print("Todas as linguagens já foram listadas.")

