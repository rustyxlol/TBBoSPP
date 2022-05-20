"""
Project 03
Mapping text onto a bitmap

Author: Rusty
GitHub: https://github.com/rustyxlol/TBBoSPP
"""
import sys


def get_bmp_format():
    "Display bitmap file containing bitmap format"
    try:
        with open('bitmap_format.txt', 'r', encoding='utf8') as bmp_format:
            return bmp_format.read()

    except FileNotFoundError:
        print("Bitmap Format File not found!")

    return None


def text_to_bmp(text, bmp):
    "Converts text to bitmap format"
    result = ""
    text_len = len(text)
    for index, bit in enumerate(bmp):
        if bit in ('*', '.'):
            result += text[index % text_len]
        else:
            result += bit
    with open('output.txt', 'w', encoding='utf8') as outfile:
        outfile.write(result)

    print(result)


def main():
    user_input = input("Enter message to map: ")
    if len(user_input.strip()) == 0:
        sys.exit()

    bitmap_format = get_bmp_format()
    if bitmap_format is not None:
        text_to_bmp(user_input, bitmap_format)
        print("You can also find this in output.txt")


if __name__ == "__main__":
    main()
