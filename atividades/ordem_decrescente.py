"""
     Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente
"""

def print_numeros_ordem_decrescente():
     for i in range(10, 0, -1): # range(numero inicial, numero q sera interrompido o for, intervalo que sera percorrido)
          print(i)

if __name__ == '__main__':
     print_numeros_ordem_decrescente()