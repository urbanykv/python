#Estruturas de repetição

'''
   Enquanto algo, processar: O bloco de operações será executado enquanto a condição 'algo' for verdadeira.

   Até que algo, processar: O bloco de operações será executado até que a condição 'algo' seja verdadeira. 

   Processar, enquanto algo: Nesse tipo de estrutura, primeiramente o bloco é executado.
   Caso a condição seja verdadeira, o bloco é executado novamente e caso seja falso o bloco é encerrado.

   Processar, até que algo: Neste tipo de estrutura, primeiramente o bloco é executado, e somente depois é realizado o teste da condição.
   O bloco é executado até que a condição se torne verdadeira.
   
   Para: Primeiro é verificada se a condição é verdadeira, depois é executado o bloco de comandos. SErão novamente checados e executados enquanto a condição for verdadeira.
'''

'''A estrutura de repetição for tem funcionamento muito semelhante nas linguagens C e Python. Contudo, a sintaxe é diferente nas duas linguagens. Além disso, existe mais flexibilidade em Python, já que a repetição pode ser controlada por uma variável não numérica.'''

'''Antes de detalharmos o for, vamos conhecer uma função de Python que gera uma lista de valores numéricos. Essa lista nos ajudará a verificar a repetição e deixará mais claro o entendimento do laço. range()'''

#Ela se encontra em Python Básico/10 - Objetos Range/AL10.py

#Estruturas de repetição for
for num in range(2,9,3):
    print(num)

    #Primeiro Numero é o Parâmetro start, o segundo é o Parâmetro End e o ultimo é o Step.

##Estruturas de repetição for com string
nome = input("Entre com o seu nome: \n")

for letra in nome:
    print(letra)

#Estruturas de repetição while

palavra = input('Entre com uma palavra: \n ')
while palavra != 'sair':
    palavra = input('Digite sair para encerrar o laço: \n')
print('Você digitou sair e agora está fora do laço')

#As instruções auxiliares break, continue e pass (while)

#A instrução break
while True:
    palavra = input('Entre com uma palavra: \n')
    if palavra == 'sair':
        break
print('Você digitou sair e agora está fora do laço')

'''Caso haja vários laços aninhados, o break será relativo ao laço em que estiver inserido.'''

#A instrução continue

'''A instrução continue também funciona da mesma maneira em C e em Python. Ela atua sobre as repetições dos laços for e while, como a instrução break, mas não interrompe todas as repetições do laço. Essa instrução interrompe apenas a iteração corrente, fazendo com que o laço passe para a próxima iteração.

O exemplo a seguir imprime todos os números inteiros de 1 até 10, pulando apenas o 5. Veja sua implementação (código 8 do arquivo disponibilizado) no emulador abaixo:'''

for num in range(1,11):
    if num == 5:
        continue
    else:
        print(num)
print("Laço encerrado")

'''Para ressaltar a diferença entre as instruções break e continue, vamos alterar a linha 3 do código anterior, trocando a instrução continue pela instrução break. Clique em Executar no emulador e veja a nova execução. Essa alteração está no arquivo disponibilizado neste texto (código 9).'''

#A instrução pass
'''A instrução pass atua sobre a estrutura if, permitindo que ela seja escrita sem outras instruções a serem executadas caso a condição seja verdadeira. Assim, podemos concentrar as instruções no caso em que a condição é falsa.

Suponha que queiramos imprimir somente os números ímpares entre 1 e 10. Uma implementação possível está no emulador seguinte (código 10 do arquivo disponibilizado):'''

for num in range(1, 11):
    if num % 2 == 0:
        pass
    else:
        print(num)
print('Laço encerrado')

'''Claramente, seria possível reescrever a condição do if-else para que pudéssemos transformá-lo em um if simples, sem else. Entretanto, o objetivo aqui é mostrar o uso da instrução pass.

Agora que já vimos os principais conceitos relativos às estruturas de decisão e de repetição, vamos testar seus conhecimentos.'''