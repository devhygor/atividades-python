import os
"""
    1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.

    2 - Utilizando o dicionário criado no item 1:

    Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
    Adicione um campo de profissão para essa pessoa;
    Remova um item do dicionário.
"""

# A parte de adcionar e remover irei fazerno futuro

pessoas_list = []

def home_controller():
    limpar_console()
    titulo_paginas('PAGINA PRINCIPAL')
    opcao_escolhida = escolher_opcao()
    match opcao_escolhida:
        case 1:
            limpar_console()
            listar_pessoas_cadastradas()
        case 2:
            limpar_console()
            cadastrar_pessoa()
        case 3:
            limpar_console()
            atualizar_pessoa()
        case _:
            return('Aplicativo Encerrando')

def escolher_opcao():
    print('''OPÇÕES:
1 - Listar as pessoas cadastradas
2 - Cadastrar uma nova pessoa
3 - Modificar algum valor
4 - Adcionar um campo para a pessoa
5 - Remover uma pessoa
Qualquer outro valor para sair do programa\n''')
    opcao_desejada = int(input('Digite a opção que desejar: '))
    return opcao_desejada

def listar_pessoas_cadastradas():
    titulo_paginas('LISTAR PESSOAS CADASTRADA')
    if len(pessoas_list) > 0:
        for i in pessoas_list:
            print(i)
    else:
        print('\nNão tem pessoas cadastrada')
    
    input('Pressione enter para voltar ao menu principal')
    home_controller()

def cadastrar_pessoa(mais_execucao=False):
    if not mais_execucao:
        limpar_console()
        titulo_paginas('CADASTRO DE PESSOA')
    nome = input('Digite o nome da pessoa: ')
    idade = input('Digite a idade: ')
    cidade =input('Digite a cidade: ')
    pessoas_list.append({
        'nome': nome,
        'idade': idade,
        'cidade': cidade,
    })
    continuar_cadastro = input('Deseja continuar cadastrando mais pessoas? S/N: ').lower()
    if continuar_cadastro == 's':
        cadastrar_pessoa(mais_execucao=True)
    else:
        home_controller()

def atualizar_pessoa():
    limpar_console()
    titulo_paginas('ATUALIZAR CADASTRO DA PESSOA')
    nome_pessoa = input('Digite o nome da pessoa que você quer editar ')
    pessoa_que_sera_atualizada = ''
    for dict_pessoa in pessoas_list:
        if dict_pessoa['nome'] == nome_pessoa:
            campos_disponiveis = list(dict_pessoa.keys())
            print(f'\nCampos disponiveis para atualizar: {campos_disponiveis}')
            campo = ''
            while campo not in campos_disponiveis:
                campo = input(f'\nEscolha uma das opçoes disponiveis para atualizar da {nome_pessoa}: ')
            novo_valor = input(f'\nDigite o novo valor que o campo {campo} irá receber ')
            dict_pessoa[campo] = novo_valor
            print(f'\nPessoa atualizada com sucesso!!!')
            break

    input('Digite uma tecla para voltar ao menu principal: ')
    home_controller()

def limpar_console():
    os.system('clear')

def titulo_paginas(titulo):
    tamanho = len(titulo)
    print('*' * tamanho)
    print(titulo)
    print('*' * tamanho)
    print()
    
if __name__ == '__main__':
    home_controller()