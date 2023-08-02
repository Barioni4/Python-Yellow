def encontrar_maior_menor_numero(sequencia):
    if not sequencia:
        raise ValueError("A sequência está vazia. Não é possível encontrar o maior e o menor número.")

    maior = menor = sequencia[0]

    for numero in sequencia:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero

    return maior, menor

def main():
    try:
        sequencia = [float(num) for num in input("Digite a sequência de números separados por espaço: ").split()]
        maior, menor = encontrar_maior_menor_numero(sequencia)
        print(f"Maior número: {maior}")
        print(f"Menor número: {menor}")
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar apenas números separados por espaço.")

if __name__ == "__main__":
    main()