from generate_password import generate_password


def main():
    length = int(input("Qual o comprimento da senha? "))
    password = generate_password(length)
    print(f"Sua senha gerada é: {password}")

if __name__ == "__main__":
    main()