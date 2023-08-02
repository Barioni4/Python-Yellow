def ordenar_crescente_inplace(lista_numeros):
    lista_numeros.sort()

def main():
    lista_numeros = [float(num) for num in input("Digite a lista de números separados por espaço: ").split()]
    ordenar_crescente_inplace(lista_numeros)
    print("Lista ordenada em ordem crescente:", lista_numeros)

if __name__ == "__main__":
    main()

def ordenar_crescente(lista_numeros):
    return sorted(lista_numeros)

def main():
    lista_numeros = [float(num) for num in input("Digite a lista de números separados por espaço: ").split()]
    lista_ordenada = ordenar_crescente(lista_numeros)
    print("Lista ordenada em ordem crescente:", lista_ordenada)

if __name__ == "__main__":
    main()