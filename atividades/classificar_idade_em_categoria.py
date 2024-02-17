"""
    Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

    Criança: 0 a 12 anos;
    Adolescente: 13 a 18 anos;
    Adulto: acima de 18 anos.
"""

def input_idade():
    idade = int(input('Digite a sua idade: '))
    return idade

def categorizar_idade(idade):
    if idade >= 0 and idade <= 12:
        categoria = 'Criança'
    elif idade >= 13 and idade <= 18:
        categoria = 'Adolescente'
    else:
        categoria = 'Adulto'
    return categoria

def resposta_categoria(categoria, idade):
    print(f'\n A idade digitada foi "{idade}", que se enquadra na categoria "{categoria}".')

def main():
    idade = input_idade()
    categoria = categorizar_idade(idade)
    resposta_categoria(categoria, idade)

if __name__ == '__main__':
    main()
