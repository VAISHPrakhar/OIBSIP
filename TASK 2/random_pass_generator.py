import random
import string

def generate_password(length, use_letters, use_digits, use_symbols):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_digits:"yes"

    characters += string.digits
    if use_symbols:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

answer = input("Do you want to generate a password? (yes/no): ")
if answer.lower() == "yes":
    length = int(input("Enter the length of the password: "))
    use_letters = input("Include letters? (yes/no): ").lower() == "yes"
    use_digits = input("Include digits? (yes/no): ").lower() == "yes"
    use_symbols = input("Include symbols? (yes/no): ").lower() == "yes"
    print(generate_password(length, use_letters, use_digits, use_symbols))