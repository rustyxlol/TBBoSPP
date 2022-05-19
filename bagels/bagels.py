import random
from tabnanny import check


def generate_number():
    return str(random.randint(100, 999))


def checkInput(number, random_number):
    if list(number) == list(random_number):
        print("Winner!")
        return "Winner"

    if number[0] == random_number[0] or number[1] == random_number[1] or number[2] == random_number[2]:
        print("Fermi")
        return "Fermi"

    if number[0] in random_number or number[1] in random_number or number[2] in random_number:
        print("Pico")
        return "Pico"

    print("Bagels")
    return "Bagels"


def game():
    tries = 10
    random_number = generate_number()

    print(random_number)

    while tries > 0:
        user_input = input("Enter a guess: ")
        if checkInput(user_input, random_number) == "Winner":
            return
        else:
            tries -= 1

    if tries == 0:
        print("You ran out of tries :(")


game()
