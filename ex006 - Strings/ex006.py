#Variáveis Strings

#Aspas Simples
nome1 = ('Matheus')

nome1.upper()

#Aspas Duplas
nome2 = ("Giulia")

nome2.lower

#Aspas Simples Triplas
nome3 = ('''Rebeca''')

nome3.split

#Aspas Duplas Triplas
nome4 = ("""Pércio""")

print(nome1.upper, nome2, nome3, nome4)

'''É possível armazenar letras, números, espaços, pontuação e diversos símbolos. Diferentemente da linguagem C, não existe o tipo char. Cada caractere em Python é uma string.'''


#Upper, Lower, Capitalize, Title e Split

curso = ('Ensino a Distância')

curso_maiusculo = curso.upper() #UPPER (Maiúsculo)

curso_minusculo = curso.lower() #lower (Minúsculo)

curso_inicial_min = curso.capitalize() #cAPITALIZE (letra inicial menor)

curso_inicial_max = curso.title() #Title (Letra inicial maior)

curso_substrings = curso.split() #Split ('substrings', 'na', 'area')

print(curso_maiusculo)
print(curso_minusculo)
print(curso_inicial_min)
print(curso_inicial_max)
print(curso_substrings)

