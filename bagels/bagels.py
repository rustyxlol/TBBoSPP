"""
Bagels game from The Big Book of Small Python Projects

Author: Rusty
GitHub: https://github.com/rustyxlol/TBBoSPP
"""
import random

MAX_GUESSES = 10


def generate_number():
    "Generate random number in a string format"
    return str(random.randint(100, 999))


def check_guess(guess_number, random_number):
    "Bagels logic"
    if guess_number == random_number:
        return "Winner"

    results = []

    for number, index in enumerate(guess_number):
        if guess_number[index] == random_number[index]:
            results.append("Fermi")
        elif number in random_number:
            results.append("Pico")

    if len(results) == 0:
        return "Bagels"

    return " ".join(results)


def game():
    "Main game loop"
    while True:
        print('''
In *Bagels*, a deductive logic game, you
must guess a secret three-digit number based on clues.   
The game offers one of the following hints in response to your guess:

1. "Pico" when your guess has a correct digit in the wrong place 
2. "Fermi" when your guess has a correct digit in the correct place  
3. "Bagels" if your guess has no correct digits. 
You have 10 guesses to guess the secret number.
''')
        guesses = MAX_GUESSES
        random_number = generate_number()

        print("I have thought of a number")

        while guesses > 0:
            print(f"You have {guesses} guesses left")
            user_input = input("Enter a guess: ")

            while len(user_input) != len(random_number):
                user_input = input("Enter a guess that is three digits: ")

            result = check_guess(user_input, random_number)
            print(result)

            if user_input == random_number:
                break

            guesses -= 1

        if guesses == 0:
            print("You ran out of guesses :(")
            print(f"The number was: {random_number}")

        play_again = input("Do you want to play again(y/n)?: ")

        if play_again.lower() != 'y':
            break

    print("Thanks for playing!")


if __name__ == "__main__":
    game()
