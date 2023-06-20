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

for num in range(1, 11):
    if num % 2 == 0:
        pass
    else:
        print(num)
print('Laço encerrado')