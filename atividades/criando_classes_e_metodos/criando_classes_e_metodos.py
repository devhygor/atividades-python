# Exercícios
# Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.
class Livro():
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

# Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.
    def __str__(self) -> str:
        return f'Titulo: {self.titulo}, Autor: {self.autor}, Ano Publicação: {self.ano_publicacao}, esta disponivel? {self.disponivel}'

# Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.
    def emprestar(self):
        self.disponivel = False

# Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.
    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro.ano_publicacao == ano and livro.disponivel]
        return livros_disponiveis

# Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.
    # em outro arquivo

# No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.
    # em outro arquivo

# No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.
    # em outro arquivo

# Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos da classe Livro e exiba a mensagem formatada utilizando o método str.


livro1 = Livro('Lagoa Azul', 'Autor qualquer', 1996)
print(livro1)
livro2 = Livro('Nome Filme 2', 'Nome do Segundo Autor', 2000)
print(livro2)

livro3 = Livro("Python Cookbook", "Samuel Developer", 2019)
print(f"Antes de emprestar: Livro disponível? {livro3.disponivel}")
livro3.emprestar()
print(f"Depois de emprestar: Livro disponível? {livro3.disponivel}")

Livro.livros = [livro1, livro2, livro3]