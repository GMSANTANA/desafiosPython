# Crie um script que tenha a idade de uma pessoa em uma
# variável,depois faça a concatenação da idade com duas "strings"
# adicionando o valor de ambos a outra nova variável, ex: nova
# ="parabéns"+idade+"anos" vai ocorrer um error, então tente
# resolver e explique pq isso acontece.

idade = 20
print("parabens, pelos " + idade + " " + "anos")
# vai ocorrer o erro pois o python vai inteder que idade e uma string e não uma numero
# para nos transformarmos uma variavel em numeros vamos utilizar str(variavel)
# vai ficar dessa maneira o correto!
print("parabens, pelos " + str(idade) + " " + "anos")