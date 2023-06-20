#Range
x = 50
for n in range(x):
    print(n)

'''As listas do tipo range()
Ao chamar o método range(), Python cria uma sequência de números inteiros, desde uma maneira simples até a mais complexa.'''

'''Simples
Ela pode ser chamada de maneira simples, tendo apenas com um argumento. Nesse caso, a sequência começará em 0 e será incrementada de uma unidade até o limite do parâmetro passado (exclusive). Exemplo: range(3) cria a sequência (0, 1, 2).'''

'''Não iniciadas em 0
Para que a sequência não comece em 0, pode-se informar o início e o fim como parâmetros. Lembre-se de que o parâmetro fim não entra na lista (exclusive o fim). O padrão é incrementar cada termo em uma unidade. Ou seja, a chamada range(2, 7) cria a sequência (2, 3, 4, 5, 6).'''

'''Indicando início, fim e passo
Também é possível criar sequências mais complexas indicando, na ordem, os parâmetros de início, fim e passo. O passo é o valor que será incrementado de um termo para o próximo. Exemplo: range(2, 9, 3) cria a sequência (2, 5, 8)'''