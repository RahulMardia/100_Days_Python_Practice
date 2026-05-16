from art import logo

print(logo)

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

cipher_again = True


def encrypt(original_text, shift_amount):
    encrypted_text = ""

    for char in original_text.lower():
        # Keep spaces, numbers, and symbols unchanged
        if char not in alphabet:
            encrypted_text += char
        else:
            index = alphabet.index(char) + shift_amount
            index %= len(alphabet)
            encrypted_text += alphabet[index]

    print(f"Encrypted text: {encrypted_text}")
    restart()


def decrypt(original_text, shift_amount):
    decrypted_text = ""

    for char in original_text.lower():
        # Keep spaces, numbers, and symbols unchanged
        if char not in alphabet:
            decrypted_text += char
        else:
            index = alphabet.index(char) - shift_amount
            index %= len(alphabet)
            decrypted_text += alphabet[index]

    print(f"Decrypted text: {decrypted_text}")
    restart()


def caesar():
    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    else:
        print("Invalid input. Please type 'encode' or 'decode'.")


def restart():
    global cipher_again
    go_again = input(
        "Type 'yes' if you want to go again. Otherwise type 'no': "
    ).lower()

    if go_again == "yes":
        cipher_again = True
    else:
        cipher_again = False
        print("Good Bye!")


while cipher_again:
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n"
    ).lower()

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Handle shift values greater than 26
    shift %= len(alphabet)

    caesar()