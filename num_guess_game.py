import random

def guess_number():
    number_guess=random.randint(1,10)
    print("guess the number between  1 to 10")
    print("lets chech your luck")
    atempt=0
    while True:
        try:
            guess=int(input("enter the guess number: "))
            atempt=+1
            if guess<number_guess:
                print("its wrong try the largest number")
            elif guess>number_guess:
                print("its wrong try the smalest number")
            else:
                print(f"{number_guess} thats right congrats you won the game")
                break
        except ValueError:
            print("invalid number")

guess_number()
