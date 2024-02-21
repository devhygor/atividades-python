"""
    Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos.
    Utilize um bloco try-except para lidar com possíveis exceções.
"""

def input_numeros():
    lista_numeros = []

    while True:
        entrada = input("Digite um número (ou pressione Enter para encerrar): ")

        if entrada == "":
            break

        try:
            numero = float(entrada)
            lista_numeros.append(numero)

        except ValueError:
            print("Erro: Certifique-se de inserir apenas números.")

    soma = sum(lista_numeros)

    print("Lista de números:", lista_numeros)
    print("A soma dos números na lista é:", soma)
    
if __name__ == '__main__':
    input_numeros()
