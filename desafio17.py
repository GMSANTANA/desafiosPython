# Crie um script que remova o ultimo elemento da lista com metodo .pop(),
# armazene em uma segunda variavel, e faça a concatenação dele com uma frase
# "string" que comece com a primeira letra maiúscula.

carros = ['hb20', 'onix', 'ka+', 'golf']
print(carros)

carros_batidos = carros.pop()

print("Qual foi o carro batido? " + " \nfoi um " + carros_batidos.title() + " !! ")

