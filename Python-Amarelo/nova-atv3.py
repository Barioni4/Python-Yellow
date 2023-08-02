def imprimir_numeros_naturais(n):
    for i in range(n + 1):
        print(i)

def main():
    try:
        numero = int(input("Digite um número inteiro positivo: "))
        if numero < 0:
            print("Por favor, digite um número inteiro positivo.")
        else:
            imprimir_numeros_naturais(numero)
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar um número inteiro positivo.")

if __name__ == "__main__":
    main()