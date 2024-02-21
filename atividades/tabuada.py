"""
    Solicite ao usuário um número e, em seguida, 
    utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
"""

def input_numero():
    numero = int(input('Digite um numero: '))
    return numero

def multiplicar(numero):
    for i in range(1, 11):
        valor = numero * i
        print(f'O valor de {numero} x {i} = {valor}')

if __name__ == '__main__':
    numero = input_numero()
    multiplicar(numero)