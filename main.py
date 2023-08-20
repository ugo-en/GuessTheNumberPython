from random import randint

comp_number = randint(1, 10)  # this is the number the computer chose
guess = None

while guess != comp_number:
    guess = int(input("Guess the number from 1 to 10: "))
    if guess < comp_number:
        print("Too low!")
    elif guess > comp_number:
        print("Too high!")
    else:
        print("Congratulations! You guessed correctly!")
