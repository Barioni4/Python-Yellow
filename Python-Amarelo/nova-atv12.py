def calcular_mediana(lista_numeros):
    lista_ordenada = sorted(lista_numeros)
    tamanho_lista = len(lista_ordenada)

    if tamanho_lista % 2 == 1:
        # Lista com número ímpar de elementos
        mediana = lista_ordenada[tamanho_lista // 2]
    else:
        # Lista com número par de elementos
        meio1 = lista_ordenada[tamanho_lista // 2 - 1]
        meio2 = lista_ordenada[tamanho_lista // 2]
        mediana = (meio1 + meio2) / 2

    return mediana

def main():
    try:
        lista_numeros = [float(num) for num in input("Digite a lista de números separados por espaço: ").split()]
        mediana = calcular_mediana(lista_numeros)
        print(f"Mediana dos valores: {mediana}")
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar apenas números separados por espaço.")

if __name__ == "__main__":
    main()