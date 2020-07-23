#EXEMPLO DE EXTRUTURAS DE ERROS TRY E EXCEPT
#usamos para tentar rodar o código.
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
#usamos o 'exceto' para se caso o código falhar.
except:
    print('Infelizmente tívemos um problema... :{')
#usamos o else para confirmar que o código rodou.
else:
    print(f'O resultado é {r:.1f}')
#a função finally vai acontecer sempre(se der errado ou se der certo)
finally:
    print('Volte sempre!')
#obs: um mesmo 'try' pode ter vários 'except'.
#as funções 'else' e 'finally' são opcionais dependendo do contexto do código.

