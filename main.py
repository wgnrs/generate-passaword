from password_generator import generate_password


def main():
    length = input("What's the length of password? ")

    # validation if input is not a digit
    if not length.isdigit():
        print("You need put a number!")
        return

    length = int(length)

    password = generate_password(length)
    print(f"Sua senha gerada é: {password}")


if __name__ == "__main__":
    main()
