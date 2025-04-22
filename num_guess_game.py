import random

def guess_number():
    number_guess=random.randint(1,100)

    while True:
        try:
            guess=int(input("enter the guess number: "))
            atempt=+1
            if guess<number_guess:
                print("its wrong try the largest number")
            elif guess>number_guess:
                print("its wrong try the smalest number")
            else:
                print("thats right you won the game")
                break
        except ValueError:
            print("invalid number")

guess_number()
