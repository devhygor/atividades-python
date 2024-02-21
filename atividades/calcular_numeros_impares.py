"""
    Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
"""

def calcular_numeros_impares():
    resultado = 0
    for i in range(10):
        if not i % 2 == 0:
            resultado += i
    
    print(f'Resultado = {resultado}')

if __name__ == '__main__':
    calcular_numeros_impares()