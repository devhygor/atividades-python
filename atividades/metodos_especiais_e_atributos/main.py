# Em um arquivo chamado main.py, importe a classe Carro.
from metodos_especiais_e_atributos import Carro

# No arquivo main.py, instancie três objetos da classe Carro com diferentes características, como marca, modelo e cor.
carro1 = Carro('Ford', 'New Fiesta', 'Branco')
carro2 = Carro('Ford', 'Fusion', 'Preto')
carro3 = Carro('Chevrolet', 'Onix', 'Azul')

print(f"Carro 1: {carro1.marca} {carro1.modelo}, Cor: {carro1.cor}")
print(f"Carro 2: {carro2.marca} {carro2.modelo}, Cor: {carro2.cor}")
print(f"Carro 3: {carro3.marca} {carro3.modelo}, Cor: {carro3.cor}")