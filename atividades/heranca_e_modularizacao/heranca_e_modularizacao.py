# Com base no que vimos nessa aula sobre herança, crie uma classe Banco com dois atributos: nome e endereco. Em seguida, derive uma classe chamada Agencia que herda os atributos da classe Banco e inclua um atributo adicional chamado numero. Ambas as classes devem ter apenas o construtor.

class Banco():
    def __init__(self, nome, endereco) -> None:
        self.nome = nome
        self.endereco = endereco


class Agencia(Banco):
    def __init__(self, nome, endereco, numero) -> None:
        super().__init__(nome, endereco)
        self.numero = numero