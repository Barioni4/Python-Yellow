def numeros_pares(lista):
    numeros_pares = [num for num in lista if num % 2 == 0]
    return numeros_pares

def main():
    try:
        lista_numeros = [int(num) for num in input("Digite a lista de números separados por espaço: ").split()]
        pares = numeros_pares(lista_numeros)
        print("Números pares:", pares)
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar apenas números inteiros separados por espaço.")

if __name__ == "__main__":
    main()