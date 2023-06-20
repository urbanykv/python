# def= Definições, é usado para criar função
def multiplicador(numero):
        global a
        a = 2 # esta variável tem escopo local
        print(f"Dentro da função, a variável vale: {a}")
        u = 3
        return a * numero + u

a = 3 # esta variável tem escopo global
b = multiplicador(5)
print(f"Resultado: {b}")