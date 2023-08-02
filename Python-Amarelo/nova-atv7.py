def calcular_fatorial(numero):
    if numero < 0:
        raise ValueError("Não é possível calcular negativos ou quebrados.")
    elif numero == 0:
        return 1
    else:
        fatorial = 1
        for i in range(1, numero + 1):
            fatorial *= i
        return fatorial

def main():
    try:
        numero = int(input("Digite um número: "))
        resultado = calcular_fatorial(numero)
        print(f"O fatorial de {numero} é: {resultado}")
    except ValueError:
        print("Errou. Não podemos números negativo ou quebrados.")

if __name__ == "__main__":
    main()