#Seção 3 - Exercício 01

quantidadeMinima = eval(input("Adicione a quantidade minima permitida: "))
quantidadeMaxima = eval(input("Adicione a quantidade máxima permitida: "))

somar = (quantidadeMinima + quantidadeMaxima)
dividir = (somar // 2)
estoqueMedio = (dividir)

print(f"O estoque médio é: {estoqueMedio}")

#Exercício 02

x = eval(input("Adicione o primeiro número:"))
y = eval(input("Adicione o segundo número:"))

soma = (x + y)
resultado = soma

print(resultado)

#Exercício 03

metros = eval(input("Adicione o valor em metros: "))

multiplicar = (metros * 100)
centimetros = multiplicar

print(f'Esse valor metro {metros} em centimetros é: {centimetros}')

#Exercício 04

horasTrabalhadas = eval(input('Adicione as horas trabalhadas: '))
valorHora = eval(input('Adicione o Valor pago per hora: '))

totalSalario = (horasTrabalhadas * valorHora)

print(f"O seu salário total sera de R${totalSalario}")

#Exercício 05

altura = eval(input("Adicione aqui a sua altura: "))

mult = (72.7 * altura)
sub = (mult - 58)
resultado = sub

print(f'O seu peso ideal é: {resultado}')