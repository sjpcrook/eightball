
import random
from colorama import Fore, Style

while True:
    #*Asks user for a question
    # while True:
    #     question = input("What is your question?  > ").strip()
    #     if question == "":
    #     # Check if the input is emptyif question == "":
    #         print(Fore.YELLOW + "Please ask a question to get a fortune!" + Style.RESET_ALL)
    #     else:
    #         break
    question = input("What is your question?  > ").strip()
    
    # Check if the input is empty
    if question == "":
        print(Fore.YELLOW + "Please ask a question to get a fortune!" + Style.RESET_ALL)
        continue

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

    #*Generates a random integer between 1 and 100
    random_number = random.randint(1, 100)
    #print(f"The number chosen is {random_number}") #Test

    #*Checks if the number is odd
    if random_number % 2 == 1:
        #print("This number is odd") #Test

        #*Generates a position in the bad fortunes list
        bad_fortune_number = random.randint(0, len(bad_fortunes)-1) 

        #*Test - prints the position in the list of the bad fortune chosen
        print(f"The bad position chosen is {bad_fortune_number}") 

        #* Prints the bad fortune
        print(Fore.RED + bad_fortunes[bad_fortune_number]+Style.RESET_ALL) #!make red

    else:
        #* Test
        #print("This number is even") 

        #* Generates a position in the good fortunes list
        good_fortune_number = random.randint(0, len(good_fortunes)-1)

        #* Test - prints the position in the list of the good fortune chosen
        print(f"The good position chosen is {good_fortune_number}") 

        #* Prints the good fortune
        print(Fore.GREEN + good_fortunes[good_fortune_number]+Style.RESET_ALL) #*make green


    #*Asks to play again, takes yes or no, will automatically lower case
    play_again = input("Would you like to play again? (yes/no)  > ").lower().strip()
    if play_again != "yes":
        print("Thank you for playing.")
        break


#tested whether number was odd or even, expected to say odd when odd or even when even, no matter the question
#got result
