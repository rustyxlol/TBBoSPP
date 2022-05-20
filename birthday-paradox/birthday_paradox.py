"""
Project 02
Birthday Paradox Simulation from The Big Book of Small Python Projects

Author: Rusty
GitHub: https://github.com/rustyxlol/TBBoSPP
"""

import datetime
import random


def generate_birthdays(num_birthdays):
    "Generates num_birthdays dates"
    birthdays = []

    start_date = datetime.datetime(2022, 1, 1)
    for _ in range(num_birthdays):
        random_day = datetime.timedelta(random.randint(0, 364))
        birthdays.append(start_date + random_day)

    return birthdays


def display_birthdays(birthdays):
    "Displays birthdays in a pretty format"
    for index, birthday in enumerate(sorted(birthdays)):
        print(f"{birthday.strftime('%d %B'):15}", end='')
        if index % 4 == 3:
            print()
    print()


def count_duplicate_birthdays(birthdays):
    "Returns number of recurring birthdays"
    total_birthdays = len(birthdays)
    total_unique_birthdays = len(set(birthdays))

    return total_birthdays - total_unique_birthdays


def get_duplicate_birthdays(birthdays):
    "Returns the recurring birthdays"
    seen = set()
    overlaps = []
    for birthday in birthdays:
        if birthday in seen:
            overlaps.append(birthday)
        else:
            seen.add(birthday)

    return overlaps


def run_simulation(num_birthdays, n=100_000):
    "Runs n simulations"

    total_sims_with_overlaps = 0
    for i in range(n):
        birthdays = generate_birthdays(num_birthdays)
        num_duplicates = count_duplicate_birthdays(birthdays)
        if num_duplicates > 0:
            total_sims_with_overlaps += 1
        if i % 10000 == 9999:
            print(f"{i + 1} simulations ran...")

    probability = round(total_sims_with_overlaps / 100_000 * 100, 2)
    print(
        f"Total simulations with overlapping birthdays: {total_sims_with_overlaps}")
    print(
        f"Probability of {num_birthdays} people having birthday on the \
            same day in their group: {probability}%")


def main():
    print("How many birthdays to generate? (Max 100)")
    num_birthdays = int(input("> "))

    birthdays = generate_birthdays(num_birthdays)
    print("\nThe generated birthdays are\n")
    display_birthdays(birthdays)

    num_duplicates = count_duplicate_birthdays(birthdays)
    dupe_birthdays = get_duplicate_birthdays(birthdays)

    if num_duplicates > 0:
        if num_duplicates == 1:
            print(
                f"In this simulation, there was {num_duplicates} overlapping birthday")
        else:
            print(
                f"In this simulation, there were {num_duplicates} overlapping birthdays")
        display_birthdays(dupe_birthdays)
    else:
        print("There were no overlapping birthdays in this simulation")

    sim_prompt = input("Do you wish to run 100,000 simulations?")
    if sim_prompt.lower().startswith('y'):
        run_simulation(num_birthdays)

    print("Pretty interesting stuff")


if __name__ == "__main__":
    main()
