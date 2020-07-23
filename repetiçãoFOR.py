#ESTRURURA DE REPETIÇÃO (LOOP).

#CÓDIGO PARA CRIAR UM LOOP DE ALGUMA COISA(EXEMPLO):
for oi in range(0, 11):
    print('Oi, seja bem vindo!')
#Com esse código eu executo: Oi, seja bem vindo! 10 VEZES!
#Ou seja, em vez de fazer 10 linhas de 'Print....' fazemos 2 linhas.  ;

#Se quisermos colocar por exemplo um 'input' 5 vezes...
for entrada in range(0, 5):
    input('\nDigite seu nome: ')
#SÓ PARA INDENTIFICAR QUE O PROGRAMA TERMINOU:
print('FIM')

#AGORA SE QUISER IMPRIMIR O PRÓPIO CONTADOR EM ORDEM CRESCENTE:
for contador in range(0, 11, 1):
    print(contador)
print('FIM\n')

#EM ORDEM DECRESCENTE:
for contador in range(0, 11, -1):
    print(contador)
print('FIM')
