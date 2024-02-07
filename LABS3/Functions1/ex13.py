import random

def guessthenumber():
    print("Hello! What is your name?")
    name = input()
    number = random.randint(1, 20)
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    g = 0
    while g < 6:
        print("Take a guess.")
        guess = int(input())
        g += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            break 
    if guess == number:
        print(f"Good job, {name}! You guessed my number in {g} guesses!")
    else:
        print(f"Nope. The number I was thinking of was {number}.")

guessthenumber()