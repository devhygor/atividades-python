def obter_frase():
    frase = input('Digite uma frase q iremos verificar a quantidade de palavras repetidas')
    return frase

def contar_frequencia_palavras(frase):
    # Remover pontuações e converter para minúsculas
    frase = frase.lower().replace('.', '').replace(',', '').replace('!', '').replace('?', '')
    # Dividir a frase em palavras
    palavras = frase.split()
    # Inicializar um dicionário para armazenar a frequência das palavras
    frequencia_palavras = {}
    # Contar a frequência de cada palavra
    for palavra in palavras:
        if palavra in frequencia_palavras:
            frequencia_palavras[palavra] += 1
        else:
            frequencia_palavras[palavra] = 1
    return frequencia_palavras

def imprimir_resultado(resultado):
    print("Frequência de palavras na frase:")
    for palavra, frequencia in resultado.items():
        print(f"{palavra}: {frequencia}")

def main():
    frase = obter_frase()
    frequencia = contar_frequencia_palavras(frase)
    imprimir_resultado(frequencia)

if __name__ == '__main__':
    main()