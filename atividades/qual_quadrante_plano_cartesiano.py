"""
    Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

    Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
    Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
    Terceiro Quadrante: os valores de x e y devem ser menores que zero;
    Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
    Caso contrário: o ponto está localizado no eixo ou origem.
"""

def get_coordenadas():
    coordenada_x = float(input('Digite a coordenada X: '))
    coordenada_y = float(input('Digite a coordenada Y: '))
    return coordenada_x, coordenada_y

def get_quadrante(x, y):
    if x > 0 and y > 0:
        return 'Primeiro Quadrante'
    elif x < 0 and y > 0:
        return 'Segundo Quadrante'
    elif x < 0 and y < 0:
        return 'Terceiro Quadrante'
    elif x > 0 and y < 0:
        return 'Quarto Quadrante'
    else:
        return 'O ponto está localizado no eixo ou origem'

def resposta_atividade(x, y, quadrante):
    print(f'\n O Valor de x foi "{x}" e y "{y}", portanto o quadrante é: "{quadrante}"\n')

def main():
    x, y = get_coordenadas()
    quadrante = get_quadrante(x, y)
    resposta_atividade(x, y, quadrante)

if __name__ == '__main__':
    main()