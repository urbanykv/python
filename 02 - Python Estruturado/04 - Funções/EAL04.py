#Funções

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