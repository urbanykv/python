def fatorial(n):
    if(n == 1):
        return 1
    n = n * fatorial(n - 1)
    return n
resultado = fatorial(5)
print(resultado)