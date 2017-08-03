# Crie um script que contenha uma frase em uma variável sobre
# aspas simples, e faça ocorrer o error de invalid syntax:
# faça a mesma coisa com aspas duplas, e depois explique por que o
# error acontece.

menssagem01 = "Bem vindo ao McDonald's!"
menssagem02 = 'Bem vindo ao McDonald's!'
# O erro occoreu na variavel "menssagem02" pois esta somente com 1 aspas e ela não sabe onde fecho
# quando ocorrer isso tem que colocar 2 aspas como na " menssagem01"
print(menssagem01)


# erro transmitido!
# menssagem02 = 'Bem vindo ao McDonald's!'
                                         ^
# SyntaxError: invalid syntax