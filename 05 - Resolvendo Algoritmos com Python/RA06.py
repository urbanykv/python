
numero = eval(input('Digite o número abaixo: \n'))

if(numero % 2 == 0):
    print('é par')
else:
    print('é ímpar')

nome = 'Felipe Adriano'

#id
print(id(nome))

#find
print(nome.find('Adriano'))

print(nome.lower())

a = 3
b = 3
c = 4

expressao = c * (b + a ** 2)

print(expressao)

jogos = ['GTA 5', 'Principe da Persia', 'God of War']

for jogo in jogos:
    print(jogo)