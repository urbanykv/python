#Atribuição Múltipla
a, b = 1, 2
print("Antes da Troca")
print(f"o Valos das variáveis: a={a}, b={b}")
#Primeira Troca
temp = a
a = b
b = temp
print("Primeira Troca")
print(f"O valor das variáveis: a={a}, b={b}")
a, b = b, a
#Segunda Troca
print("Segunda Troca")
print(F"O valor das variáveis: a={a}, b={b}")