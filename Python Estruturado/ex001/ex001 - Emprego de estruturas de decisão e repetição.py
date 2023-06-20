#Emprego de estruturas de decisão e repetição

#if e else

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

#Exercício 01

x = 
if(x % 2 == 0):
    resultado = ("O número é par.")
else:
    resultado = ("Seu numero é impar.")

print(resultado)

#Exercício 02
notaAluno = (input('Adicione a sua nota aqui:'))
if(notaAluno >= 7):
    resultado = ("Parabéns, você foi aprovado!")
else(notaAluno >= 5):
    resultado = ("Infelizmente você está de recuperação!")
else:
    resultado = ("Infelimente você está reprovado!")


