"""
    Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
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
    return lista_numeros

def calcular_media(lista):
    try:
        if not lista:
            raise ValueError("Erro: A lista está vazia.")

        soma = sum(lista)
        media = soma / len(lista)
        return media

    except ZeroDivisionError:
        print("Erro: Divisão por zero. A lista não pode estar vazia.")

    except ValueError as e:
        print(e)

def somar_numeros(lista_numeros):
    soma = sum(lista_numeros)
    return soma

def exibir_resultado(lista_numeros, soma_numeros_lista, media):
    print("Lista de números: ", lista_numeros)
    print("A soma dos números na lista é: ", soma_numeros_lista)
    print("O valor medio dos numeros é: ", media)
    
if __name__ == '__main__':
    lista_numeros = input_numeros()
    media = calcular_media(lista_numeros)
    soma_numeros_lista = somar_numeros(lista_numeros)
    exibir_resultado(lista_numeros, soma_numeros_lista, media)