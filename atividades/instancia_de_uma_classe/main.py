# Crie um Arquivo Main (main.py): Crie um arquivo chamado main.py no mesmo diretório que suas classes.
# criado

# Importe e Instancie Objetos: No arquivo main.py, importe as classes Carro e Moto. Em seguida, crie três instâncias de Carro e Moto com diferentes marcas, modelos, quantidade de portas e tipos.
from instancia_de_uma_classe import Carro, Moto


carro1 = Carro('ford', 'new fiesta', 5)
carro2 = Carro('ford', 'fusion', 3)
carro3 = Carro('volksvagem', 'Gol', 2)

moto1 = Moto('Suzuky', 'cg150', 'Casual')
moto2 = Moto('Yamaha', 'faize100', 'Casual')
moto3 = Moto('Suzuky', 'hornet', 'Esportiva')

# Exiba as Informações: Para cada instância, imprima no console as informações utilizando o método str.

print(carro1)
print(carro2)
print(carro3)

print(moto1)
print(moto2)
print(moto3)