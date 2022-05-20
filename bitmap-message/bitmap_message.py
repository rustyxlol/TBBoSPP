"""
Project 03
Mapping text onto a bitmap

Author: Rusty
GitHub: https://github.com/rustyxlol/TBBoSPP
"""


def display_bmp_format():
    "Display bitmap file containing bitmap format"
    try:
        with open('bitmap_format.txt', 'r', encoding='utf8') as bmp_format:
            return bmp_format.read()

    except FileNotFoundError:
        print("Bitmap Format File not found!")


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


y = display_bmp_format()

text_to_bmp('hello', y)
