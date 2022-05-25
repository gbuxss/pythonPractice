# program to guess the number generated from random number between 0-9
import random

random_num = random.randint(1, 10)
choice = 3
while choice <= 3:
    guess_num = int(input("Enter the number to guess:\n"))
    if guess_num < 10:
        if random_num == guess_num:
            print("you got the number !!!")
            break
        elif random_num > guess_num:
            print(f"random number is greater than {guess_num}")
            print("Try again !!!")
        elif random_num < guess_num:
            print(f"random number is less than {guess_num}")
            print("Try again!!")
        choice = choice - 1
        print(f"you have {str(choice)} guess left")
        if choice == 0:
            print("You loose")
            print(f"random number is :{random_num}")
            break
    else:
        print("Enter number between 1-9")
