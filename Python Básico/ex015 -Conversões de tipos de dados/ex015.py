#Conversões de tipos de dados

#Conversões implícitas
x = 5
y = 0.5
print (type(x))
print (type(y))
print(x + y)
print(type(x + y))

'''O int foi convertido para float, pois o int cabe no float, mas, o float n cabe no int.'''

print(True + y)
print(False + x)

"""No caso de valores booleanos ocorre da seguinte forma, o true vale 1 e o false 0, portanto quando vc adiciona true (1) mais o dado desejado, ocorre a soma daquela operação, o msm ocorre com o false, ou seja, true + 2 = 3, false + 2 = 2 (isso ocorre em todas as operações)."""

"""Também pode ocorrer as conversões explicitas, quando ele força que o valor seja tratado como de determinado tipo. Para isso, é necessário usar o construtor do tipo desejado, com o valor passado como parâmetro (entre parênteses)."""

print(float(2)) #Conversão de int pra float
print(int(5.5)) #Conversão de float pra int
print(float(True)) #Conversão de bool para float
print(int(True)) #Conversão de bool para int
print(bool(0)) #Conversão de int para bool
print(bool(2.2)) #Conversão de float para bool
print(str(True)) #Conversão de bool para string
print(str(244)) #Conversão de int para string
print(str(2.0)) #Conversão de float para string 
