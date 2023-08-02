def contar_ocorrencias(texto):
    palavras = texto.split()
    ocorrencias = {}

    for palavra in palavras:
        palavra = palavra.lower()
        palavra = palavra.strip(",.;!?()[]{}\"'")
        if palavra not in ocorrencias:
            ocorrencias[palavra] = 1
        else:
            ocorrencias[palavra] += 1

    return ocorrencias

def main():
    texto = input("Digite o texto: ")
    resultado = contar_ocorrencias(texto)

    print("Quantidade de ocorrências de cada palavra:")
    for palavra, quantidade in resultado.items():
        print(f"{palavra}: {quantidade}")

if __name__ == "__main__":
    main()