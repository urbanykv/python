#Funções
import math


def ehPar(n):
    r = (n % 2 == 0)
    return  r

def somarPar(lst):
    soma = 0
    for num in lst:
        if(ehPar(num)):
            soma = soma + num
    return soma

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
soma = somarPar(lst)
print(soma)



def fatorial_iterativo(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return (f)
numero = 8
print(f'fatorial de {numero} é: {fatorial_iterativo(numero)}')


a = 0
a += 1
print(a)

def somar(n1, n2):
    return n1 + n2 

print(somar(5,6))

def hello(meu_nome):
    print("Olá " + meu_nome)

hello("Fabio")

nomes =  ["Matheus", "Percio", "Giulia", "Leila"]

def helloAvancado(meu_nome):
    for nome in meu_nome:
        print(nome)

helloAvancado(nomes)

exp = math.pi

ramdom = math.radians(18000)
print(ramdom)
print(round(exp, 2)) # toFixed do Python.

nome = 'Lúcia Cavalcante'

print(nome[6:9])


lista_programadores = ['Rita', 'Mauro', 'Jonas', 'Letícia', 'Juliana', 'Guilherme']

def imprime_maiusculo(programadores):
    for programador in programadores:
        print(programador.upper())

imprime_maiusculo(lista_programadores)

nota_1 = int(input("Digite a 1ª nota: "))
nota_2 = int(input("Digite a 2ª nota: "))
nota_3 = int(input("Digite a 3ª nota: "))

media = (nota_1 + nota_2 + nota_3) / 3

if media >= 7:
   print("Aprovado")
elif media >= 6 < 7:
   print("Recuperação")
else:
   print("Reprovado")

numeros = [ 5, 6, 7 ]

[num1, num2, num3] = numeros

print(num1)

floatt = 1.5

from decimal import Decimal

numero = Decimal(0.8)

print(numero)