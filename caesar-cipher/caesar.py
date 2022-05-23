"""
Project 06
Caesar Cipher

Author: Rusty
GitHub: https://github.com/rustyxlol/TBBoSPP
"""

try:
    import pyperclip
except ImportError:
    pass


def copy_to_clipboard(text, mode):
    mode = "encrypted" if mode == "encrypt" else "decrypted"
    print(f"Full {mode} text copied to clipboard")
    pyperclip.copy(text)


def encrypt(message, shift_key):
    result = ''
    for letter in message.upper():
        if letter.isalpha():
            result += chr(((ord(letter) - 65 + shift_key) % 26) + 65)
        else:
            result += letter
    return result


def decrypt(message, shift_key):
    result = ''
    for letter in message.upper():
        if letter.isalpha():
            result += chr(((ord(letter) - 65 - shift_key) % 26) + 65)
        else:
            result += letter
    return result


def main():
    mode = ''
    translation = ''
    shift_key = 3

    # Get mode
    while True:
        print("Do you want to (e)ncrypt or (d)ecrypt?")
        action = input("> ").lower()
        if action not in ('e', 'd'):
            continue
        if action.startswith('e'):
            mode = 'encrypt'
            break
        if action.startswith('d'):
            mode = 'decrypt'
            break

    print("Enter message to encrypt")
    message = input("> ")

    # Get shift key
    while True:
        print("Enter shift key(0-25)")
        shift_key = int(input("> "))
        if shift_key <= 25:
            break

    if mode == 'encrypt':
        translation = encrypt(message, shift_key)

    if mode == 'decrypt':
        translation = decrypt(message, shift_key)

    print(translation)

    try:
        copy_to_clipboard(translation, mode)
    except ImportError:
        pass


if __name__ == "__main__":
    main()
