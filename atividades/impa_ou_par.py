'''
    Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.
'''

def input_numero_impa_ou_par():
    numero = int(input('Digite um numero para verificar se é impar ou par: '))
    return numero

def verfica_se_o_numero_e_impa_ou_par(numero):
    if numero % 2 == 0:
        resultado = f'O número {numero} é PAR'
    else:
        resultado = f'O número {numero} é IMPA'
    return resultado

def exibe_o_resultado(resultado):
    print(resultado)

def main():
    numero = input_numero_impa_ou_par()
    resultado = verfica_se_o_numero_e_impa_ou_par(numero)
    exibe_o_resultado(resultado)

if __name__ == '__main__':
    main()