import random

def lancar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2

def main():
    input("Pressione Enter para lançar os dados.")
    print("Espere estamos calculando")
    print("...")
    dado1, dado2 = lancar_dados()
    soma = dado1 + dado2
    print(f"Resultado do dado 1: {dado1}")
    print(f"Resultado do dado 2: {dado2}")
    print(f"Soma dos valores: {soma}")

if __name__ == "__main__":
    main()