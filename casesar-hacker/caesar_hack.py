"""
Project 07
Caesar Cipher Hacker

Author: Rusty
GitHub: https://github.com/rustyxlol/TBBoSPP
"""


def decrypt(message, shift_key):
    result = ''
    for letter in message.upper():
        if letter.isalpha():
            result += chr(((ord(letter) - 65 - shift_key) % 26) + 65)
        else:
            result += letter
    return result


def main():
    print("Enter message to crack")
    message = input("> ")
    print("The message could be one of the following")
    for i in range(1, 26):
        print(f"Shift key: {i:2} -", decrypt(message, i))


if __name__ == "__main__":
    main()
