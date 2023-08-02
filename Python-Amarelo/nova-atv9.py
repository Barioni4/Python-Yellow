def converter_para_maiusculas(lista_strings):
    palavras_maiusculas = [palavra.upper() for palavra in lista_strings]
    return palavras_maiusculas

def main():
    lista_strings = input("Digite uma lista de palavras separadas por espaço: ").split()
    palavras_maiusculas = converter_para_maiusculas(lista_strings)
    print(palavras_maiusculas)

if __name__ == "__main__":
    main()