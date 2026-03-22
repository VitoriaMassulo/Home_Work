
# 🔐 Question 2 – Safe Code

# i want the user to press start and than receive an randomly generated code (list) of 4 indexes from 0 to 100
# get a secret code (randint)
#what if i dont want to see the code?  ask user
# the user must enter the numbers exactly in the correct order
# to save time will make a function that tips me to (higher/lower)


import random

secret_code = [random.randint(0, 100) for n in range(4)]

check_secret_code = input("Do you want to see the secret code? (yes/no):").lower()

if check_secret_code == "yes":
    print(f"Your secret code is: {secret_code}")

input("Press Enter to start")

index = 0
tries_count = 0

def tip_hint(guess, right_code):
    if guess < right_code:
        print(f"Guess: {guesses} is too low!")
    else:
        print(f"Guess: {guesses} is too high!")

while True:

    guesses = int(input(f"Enter the number {index + 1}-th of {len(secret_code)}: "))
    tries_count += 1

    if guesses == secret_code[index]:
        index += 1
        print(f"Right guess! {index} of {len(secret_code)} is correct!")

        if index == len(secret_code):
            print(f"You win! You guessed the secret code in {tries_count} tries!")
            break

    else:
        tip_hint(guesses, secret_code[index])
        print(f"Try again")
        index = 0

