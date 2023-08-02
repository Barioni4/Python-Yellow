def calcular_media(lista_numeros):
    if not lista_numeros:
        raise ValueError("A lista está vazia. Não é possível calcular a média.")
    
    total = sum(lista_numeros)
    media = total / len(lista_numeros)
    return media

def main():
    try:
        lista_numeros = [float(num) for num in input("Digite a lista de números separados por espaço: ").split()]
        media = calcular_media(lista_numeros)
        print(f"Média dos valores: {media}")
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar apenas números separados por espaço.")

if __name__ == "__main__":
    main()