# Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.
from criando_classes_e_metodos import Livro

livro_biblioteca = Livro("Python in Practice", "Emily Coder", 2021)
print(f"Antes de emprestar (biblioteca): Livro disponível? {livro_biblioteca.disponivel}")
livro_biblioteca.emprestar()
print(f"Depois de emprestar (biblioteca): Livro disponível? {livro_biblioteca.disponivel}")

# No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.
# def main():
#     instancia_livro = Livro().emprestar
#     print(instancia_livro)

ano_especifico = 2000
livros_disponiveis_ano = Livro.verificar_disponibilidade(ano_especifico)
print(f"Livros disponíveis em {ano_especifico}: {livros_disponiveis_ano}")


# No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.
#     livros_disponiveis_no_ano = instancia_livro.verificar_disponibilidade(1996)

# if __name__ == '__main__':
#     main()