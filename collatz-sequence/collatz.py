"""
Project 12
Collatz Sequence

Author: Rusty
GitHub: https://github.com/rustyxlol/TBBoSPP
"""



def collatz(num):
    """
    The Collatz sequence is a sequence of numbers produced from a starting
    number n, following three rules:
    1. If n is even, the next number n is n / 2.
    2. If n is odd, the next number n is n * 3 + 1.
    3. If n is 1, stop. Otherwise, repeat.
    """
    print(num, end=' ')
    if num == 1:
        return
    if num % 2 == 0:
        collatz(num // 2)
    else:
        collatz((num * 3) + 1)

if __name__ == "__main__":
    collatz(27)
    print()
    