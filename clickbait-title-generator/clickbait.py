"""
Project 11
Caesar Clickbait Title Generator

Author: Rusty
GitHub: https://github.com/rustyxlol/TBBoSPP
"""
# Our website needs to trick people into looking at ads!
# Enter the number of clickbait headlines to generate:
# > 1000
# Big Companies Hate Him! See How This New York Cat Invented a Cheaper Robot
# What Telephone Psychics Don't Want You To Know About Avocados
# You Won't Believe What This North Carolina Shovel Found in Her Workplace
# --snip--
# 14 Reasons Why Parents Are More Interesting Than You Think (Number 1 Will Surprise You!)
# What Robots Don't Want You To Know About Cats
# This Florida Telephone Psychic Didn't Think Robots Would Take Her Job. She Was Wrong.

import random


OBJECT_PRONOUNS = ['Her', 'Him', 'Them']

POSSESIVE_PRONOUNS = ['Her', 'His', 'Their']

PERSONAL_PRONOUNS = ['She', 'He', 'They']

NOUNS = [
    "comparison", "education", "reflection", "music",
    "media", "resolution", "disk", "responsibility",
    "error", "policy", "reception", "strategy", ]

NAMES = [
    "Cary Leach", "Waylon Griffin", "Kenton Woodward",
    "Angeline Bowers", "Joaquin Reid", "Dana Cummings",
    "Donny Gates", "Barbra Sanders", "Sharlene Schmidt",
    "Bettye Oconnell", "Dwight Woods", "Gonzalo Berger", ]

STATES = ['California', 'Texas', 'Florida', 'New York', 'Pennsylvania',
          'Illinois', 'Ohio', 'Georgia', 'North Carolina', 'Michigan', ]

JOBS = ['Osteopath', 'Art critic', 'Landscape gardener', 'Miner'
        'Dietician', 'Pharmacist', 'Diplomat', 'Software Consultant']

PLACES = ['House', 'Attic', 'Bank Deposit Box', 'School', 'Basement',
          'Workplace', 'Donut Shop', 'Apocalypse Bunker']

WHEN = ['Soon', 'This Year', 'Later Today', 'RIGHT NOW', 'Next Week']


def cbXReasonsWhy():
    rand_number = random.randint(4, 20)
    rand_noun = random.choice(NOUNS)
    print(f"{rand_number} Reasons why {rand_noun} is INTERESTING")


def cbYouWontBelieve():
    job = random.choice(JOBS)
    print(f"You won't believe how much this {job} MAKES!")


def cbMeetName():
    name = random.choice(NAMES)
    money = random.randint(4, 9)
    place = random.choice(STATES)
    job = random.choice(JOBS)
    print(f"Meet {name}, {place} {job} WHO MAKES {money}00K per MONTH!")


def cbXIdeas():
    num = random.randint(5, 20)
    place = random.choice(PLACES)
    when = random.choice(WHEN)
    print(f"{num} Neat Ideas for Decorating your {place} {when}")


def main():
    random_functions = [cbMeetName, cbYouWontBelieve, cbXReasonsWhy, cbXIdeas]
    while True:
        print("Enter number of clickbaits to generate: ")
        n = int(input("> "))
        for i in range(n):
            random.choice(random_functions)()


if __name__ == "__main__":
    main()
