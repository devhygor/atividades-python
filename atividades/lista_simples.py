from datetime import datetime


"""
    Crie uma lista para cada informação a seguir:

    Lista de números de 1 a 10;
    Lista com quatro nomes;
    Lista com o ano que você nasceu e o ano atual.
"""


def lista_de_numeros():

    for i in range(10):
        print(i+1)
    print('\n')
    

def lista_com_quatro_nomes():
    lista_com_nomes = ['nome_um', 'nome_dois', 'nome_tres', 'nome_quatro']
    
    for nome in lista_com_nomes:
        print(nome)
    print('\n')

def lista_com_ano_nascimento_e_ano_atual():
    ano_nascimento = ['1996']
    ano_atual = datetime.now().year
    print(f'Ano nascimento: {ano_nascimento}\nAno atual: {ano_atual}')
    print('\n')
    
def main():
    lista_de_numeros()
    lista_com_quatro_nomes()
    lista_com_ano_nascimento_e_ano_atual()

if __name__ == '__main__':
    main()