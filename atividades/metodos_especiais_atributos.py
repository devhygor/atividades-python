# Exercícios

# Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.
class Carro():
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

carro01 = Carro('new fiesta', 'branco', 2014)

# Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.
# Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.
# Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.
class Restaurante():
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

    def __str__(self) -> str:
        return f'Nome restaurante = {self.nome} e sua categoria é = {self.categoria}'

restaurante01 = Restaurante('Sabor de minas', 'Comida Caseira')
print(restaurante01)

# Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.
class Cliente():
    def __init__(self, nome, idade, cpf, ativo):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.ativo = ativo

cliente01 = Cliente('Hygor', 27, '123.456.789-00', False)
cliente02 = Cliente('Patricia', 28, '321.654.987-00', False)
cliente03 = Cliente('Heloisa', 3, '000.000.000-00', True)