"""
Project 10
Cho-Han

Author: Rusty
GitHub: https://github.com/rustyxlol/TBBoSPP
"""
import random
import sys

def chohan():
    pass


def main():
    print("\n"*2)
    print("In this traditional Japanese dice game, two dice are rolled in a bamboo")
    print("cup by the dealer sitting on the floor. The player must guess if the")
    print("dice total to an even (cho) or odd (han) number.")
    print("\n")
    
    money = 5000
    
    while True:
        if money == 0:
            print("You are broke!")
            sys.exit()
        print(f"You have {money} mons, how much do you want to bet? QUIT to quit")
        bet = input("> ")
        if bet.lower().startswith('q'):
            sys.exit()
        try:
            bet = int(bet)
            if bet > money:
                print("You do not have enough mons")
                continue
        except ValueError:
            print("Please enter an integer value")
            continue
        
        print("The dealer swirls the cup and you hear the rattle of dice.")
        print("The dealer slams the cup on the floor, still covering the")
        print("dice and asks for your bet.")

        cup1 = random.randint(1, 6)
        cup2 = random.randint(1, 6)
        
        print("    CHO(even)   or   HAN(odd)")
        choice = input("> ")
        choice = choice.lower()[0]
        
        print("The dealer lifts the cup to reveal: ")
        print(f"     {cup1}-{cup2}")
        if choice in ('c', 'e'):
            if (cup1 + cup2) % 2 == 0:
                print(f"You won {bet * 2} mons")
                money += (bet * 2)
            else:
                print("You lost, sorry bro!")
                money -= bet
        
        elif choice in ('h', 'o'):
            if (cup1 + cup2) % 2 != 0:
                print(f"You won {bet * 2} mons")
                money += (bet * 2)
            else:
                print("You lost, sorry bro!")
                money -= bet
        
        else:
            print("Please enter a valid choice")
            continue
        
        
        
        

if __name__ == "__main__":
    main()
    chohan()