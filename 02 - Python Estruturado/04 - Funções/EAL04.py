#Funções



def ehPar(n):
    r = (n % 2 == 0)
    return  r

def somarPar(lst):
    soma = 0
    for num in range(lst):
        if(ehPar(num)):
            soma = soma + num
    return soma

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
soma = somarPar
print(soma)