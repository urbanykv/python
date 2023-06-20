#Emprego de estruturas de decisão e repetição

#if, elif e else

#Estratégia 01
a = 10
b = 20
if(a > b):
    maior = a
else:
    maior = b
print(f"O maior número é: {maior}")

#Estratégia 02
maior= a
if(b>maior):
    maior = b
print(f"O maior número é: {maior}")

#Exercício 01 --------//

x = 5
if(x % 2 == 0):
    resultado = ("O número é par.")
else:
    resultado = ("Seu numero é impar.")

print(resultado)

#Exercício 02 --------//
notaAluno = eval(input('Adicione a sua nota aqui:'))
if(notaAluno >= 7):
    resultado = ("aprovado!")
elif(notaAluno >= 5):
    resultado = ("recuperação!")
else:
    resultado = ("reprovado!")

print(f"status do aluno: {resultado}")

#Exercício 03 --------//
preco_unitario = 10
desconto10 = 0.1
desconto20 = 0.2
quantidadeItens = (eval(input('Adicione a quantidade de itens comprados:')))
if(quantidadeItens <= 10):
    valor_final = preco_unitario*quantidadeItens
elif(quantidadeItens <= 20):
    valor_final = preco_unitario*quantidadeItens*(1-desconto10)
else:
    valor_final = preco_unitario*quantidadeItens*(1-desconto20)
print("O valor final da compra é: {}".format(valor_final))

#Exercício 04 | Estratégia 01 --------//
lista = [10, 2, 5, 7, 6, 3]
n = len(lista)
soma = 0
for i in range(n):
    if(lista[i] % 2 == 0):
        soma = soma + lista[i]
print(f'O somatório dos elementos pares da lista é: {soma}')

#Exercício 04 | Estratégia 02 --------//
lista1 = [10, 2, 5, 7, 6, 3]
soma = 0
for num in lista1:
    if(num % 2 == 0):
        soma = soma + num
print(f'O somatório dos elementos pares da lista é: {soma}')

#Estruturas de repetição

'''A estrutura de repetição for tem funcionamento muito semelhante nas linguagens C e Python. Contudo, a sintaxe é diferente nas duas linguagens. Além disso, existe mais flexibilidade em Python, já que a repetição pode ser controlada por uma variável não numérica.'''

'''Antes de detalharmos o for, vamos conhecer uma função de Python que gera uma lista de valores numéricos. Essa lista nos ajudará a verificar a repetição e deixará mais claro o entendimento do laço. range()'''

#Ela se encontra em Python Básico/ex013 - Objetos Range/ex013.

#Estruturas de repetição for
for num in range(2,9,3):
    print(num)

    #Primeiro Numero é o Parâmetro start, o segundo é o Parâmetro End e o ultimo é o Step.

##Estruturas de repetição for com string
nome = input("Entre com o seu nome: \n")

for letra in nome:
    print(letra)

#Estruturas de repetição while

palavra = input('Entre com uma palavra: \n ')
while palavra != 'sair':
    palavra = input('Digite sair para encerrar o laço: \n')
print('Você digitou sair e agora está fora do laço')