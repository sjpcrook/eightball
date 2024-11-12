
import random
from colorama import Fore, Style



def play_again():
    '''
    A function which asks whether or not to play again, always returning "yes" or "no"
    '''
    while True:
        play_again = input("Would you like to play again? (yes/no)  > ").lower().strip()
        if play_again == "no":
            print("Thank you for playing.")
            break
        elif play_again == "yes":
            break
        else:
            print("Please respond with either yes or no.")

    #* return() is used to save the output of a function to be used elsewhere
    return(play_again) 
            

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
        continue #* continue is used to immediately restart the while loop

    #*lists of good fortunes and bad fortunes
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
        #* Test
        #print("This number is odd")

        #*Generates a position in the bad fortunes list
        bad_fortune_number = random.randint(0, len(bad_fortunes)-1) 

        #*Test - prints the position in the list of the bad fortune chosen
        #print(f"The bad position chosen is {bad_fortune_number}") 

        #* Prints the bad fortune in red
        print(Fore.RED + bad_fortunes[bad_fortune_number]+Style.RESET_ALL)

    else:
        #* Test
        #print("This number is even") 

        #* Generates a position in the good fortunes list
        good_fortune_number = random.randint(0, len(good_fortunes)-1)

        #* Test - prints the position in the list of the good fortune chosen
        #print(f"The good position chosen is {good_fortune_number}") 

        #* Prints the good fortune in green
        print(Fore.GREEN + good_fortunes[good_fortune_number]+Style.RESET_ALL)


    #*Asks to play again, takes yes or no, will automatically lower case
    # play_again = input("Would you like to play again? (yes/no)  > ").lower().strip()
    # if play_again != "yes":
    #     print("Thank you for playing.")
    #     break
    #* Uses a function to make more legible, returns either "yes" or "no"
    answer = play_again() 
    if answer == "no":
        #*The while loop breaks if the user says no, so the script ceases.
        break
    #*If the answer is yes, the script repeats

