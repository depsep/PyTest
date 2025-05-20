import random
import time
import math
from colorama import Fore, Back, Style

def main():
    rn1 = random.randrange(1, 50)
    rn2 = random.randrange(1, 10)

    rn = round(rn1 / rn2 * math.pi) #divide the number1 by number2 then round it by tenths
    cheatmode = str(input("Enable cheat mode? Y or N = "))
    if cheatmode == "Y":
        print("Cheat mode enabled")
        print(str(rn) + "\n\n")
    

    print("Guess a number from 0 to 50.")

    chosen = int(input("Guess = ")) #capture the number inputted on the user side

    print(f"You chose {chosen}")
    print("You chose...")
    time.sleep(2)
    if chosen == rn:
        print(Fore.GREEN + "Correct!")
        time.sleep(2)
        print(Fore.GREEN + "Great job!")
    else:
        print(Fore.RED + "Wrong :(")
        time.sleep(2)
        print(Fore.RED + "Sorry.")
    time.sleep(1)
    print(Fore.RESET + f"Answer was: {rn}")
    time.sleep(1) #let player see it quickly before it closes

main()