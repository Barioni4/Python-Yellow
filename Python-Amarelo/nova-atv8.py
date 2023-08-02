def encontrar_maior_menor_palavra(lista_palavras):
    if not lista_palavras:
        raise ValueError("A lista de palavras está vazia.")

    maior_palavra = menor_palavra = lista_palavras[0]

    for palavra in lista_palavras:
        if len(palavra) > len(maior_palavra):
            maior_palavra = palavra
        elif len(palavra) < len(menor_palavra):
            menor_palavra = palavra

    return maior_palavra, menor_palavra

def main():
    try:
        lista_palavras = input("Digite uma lista de palavras separadas por espaço: ").split()
        maior, menor = encontrar_maior_menor_palavra(lista_palavras)
        print(f"Maior palavra: {maior}")
        print(f"Menor palavra: {menor}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()