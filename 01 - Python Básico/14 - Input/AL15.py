#Input, é usado para entrada de dados.

nome = input("Entre com o seu nome: ")
print(nome)

#Exemplo novo
numero = input("Entre com um inteiro: ")
numero = numero + 2

#Mais um exemplo, nesse caso o usuário digitou 3 e [ENTER]. Mesmo sendo um valor, a variável numero trata como a string ‘3’. Isso impede que seja realizada a operação de soma com o inteiro 2, por exemplo. Poderíamos também usar a instrução print(type(numero)) na linha 2 para confirmar.

'''A função eval()
A função eval() recebe uma string, mas trata como um valor numérico.'''

numero = eval(input("Entre com um inteiro: "))
numero = numero + 2
print(numero)




