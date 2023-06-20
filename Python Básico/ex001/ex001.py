a = 0
for i in range(30):
    if a % 2 == 0:
        a += 1
        continue
    else:
        if a % 5 == 0:
            break
        else:
            a += 3
print (a)

nome = "Exemplo de String em Python"
print(nome)
print('valor da variável nome= {}'.format(nome))

# adicionando comments

"""Adicionando mais comments, dessa vez é um comments grande!!!!!!!!!!!!"""