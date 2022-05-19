import random
from tabnanny import check

MAX_GUESSES = 10


def generate_number():
    return str(random.randint(100, 999))


def checkInput(number, random_number):
    if number == random_number:
        return "Winner"

    results = []

    for i in range(len(random_number)):
        if number[i] == random_number[i]:
            results.append("Fermi")
        elif number[i] in random_number:
            results.append("Pico")

    if len(results) == 0:
        return "Bagels"
    else:
        return " ".join(results)


def game():
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

            result = checkInput(user_input, random_number)
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
