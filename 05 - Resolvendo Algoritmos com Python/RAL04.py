#Seção 7 - Exercício 01

maior = 0
valor = eval(input('Digite um número aq =>'))

while(valor != 0): #Processe
    if(valor > maior):
        maior = valor
    valor = eval(input('Digite um número aq =>'))
print(f'Maior valor: {maior}')

#Exercício 02

for i in range(1,101):
    print(i)
    if(i % 10 == 0):
        print(f'Multiplo de 10: {i}')

#Exercício 03

for a in range(100,201):
    if(a % 2 != 0):
        print("Impar:{}".format(a))

