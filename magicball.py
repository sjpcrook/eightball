
import random
from colorama import Fore, Style

input("What is your question?  > ") #*Asks user for a question

#lists of good fortunes and bad fortunes
good_fortunes = [
    "You will have a good day.",
    "Something good will happen today",
    "You will have good fortune."
    ]

bad_fortunes = [
    "You will have a bad day.",
    "Something bad will happen today",
    "You will have bad fortune."
    ]

random_number = random.randint(1, 100) #*Generates a random integer between 1 and 100
print(f"The number chosen is {random_number}") #Test
if random_number % 2 == 1: #*Checks if the number is odd
    #print("This number is odd") #Test
    bad_fortune_number = random.randint(0, len(bad_fortunes)-1) #*Generates a position in the bad fortunes list
    print(f"The bad position chosen is {bad_fortune_number}") #*Test - prints the position in the list of the bad fortune chosen
    print(f"Your fortune is: {bad_fortunes[bad_fortune_number]}") #* Prints the bad fortune
else:
    #* Test
    #print("This number is even") 

    #* Generates a position in the good fortunes list
    good_fortune_number = random.randint(0, len(good_fortunes)-1)

    #* Test - prints the position in the list of the good fortune chosen
    print(f"The good position chosen is {good_fortune_number}") 

    #* Prints the good fortune
    print(f"Your fortune is: {good_fortunes[good_fortune_number]}") 

#play_again = input("Would you like to play again?  > ").lower()
#if play_again == "yes":
    #loop

#tested whether number was odd or even, expected to say odd when odd or even when even, no matter the question
#got result
