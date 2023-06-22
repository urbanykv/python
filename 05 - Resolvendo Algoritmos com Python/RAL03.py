#Seção 6 - Exercício 01

n = eval(input('Adicione um número: '))

if(n > 100):
    print(n)
else:
    print(0)

#Exercício 02

valor = eval(input("Informe um número:"))

if(valor > 0):
    a = valor
    print(f'Valor positivo: {a}')
else:
    b = valor
    print(f'Valor negativo: {b}')

#Exercício 03 - Estratégia 01

valor = eval(input("Informe um número:"))
if(valor % 2 == 0):
    p = valor
    print(f'Seu número é par: {p}')
else:
    i = valor
    print(f'Seu número é impar: {i}')

#Exercício 03 - Estratégia 02

i = 0
p = 0

valor = eval(input("Informe um número:"))
if(valor % 2 == 0):
    p = valor
else:
    i = valor

print(f'Seu número par é: {p}')
print(f'Seu número impar é: {i}')

#Exercício 04

altura = eval(input("Adicione aqui a sua altura: "))
sexo = input('Informe seu sexo Masculino(M) ou Feminino(F): ')

if(sexo == 'M'):
    mult = (72.7 * altura)
    sub = (mult - 58)
    resultado = sub
    
elif(sexo == 'F'):
    mult = (62.1 * altura)
    sub = (mult - 44.7)
    resultado = sub
    print(f'O seu peso ideal é: {resultado}')
else:
    print('Sexo não reconhecido.')



#Exercício 05



#Exercício 06



#Exercício 07



#Exercício 08



#Exercício 09



#Exercício 10