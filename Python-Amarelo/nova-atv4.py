def palindromo(palavra):
    palavra = palavra.lower().replace("","")
    return palavra == palavra[::-1]

def main():
    palavra = input("Digite uma palavra: ")

    if palindromo(palavra):
        print("Oxe, que legal! É um palindromo.")
    else:
        print("Que pena, é uma palavra normal...")

if __name__ == "__main__":
    main()