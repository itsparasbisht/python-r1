import random

number = random.randint(1,9)
attempts = 0

print("\n----------Hey you, guess the number between 1 - 10-----------\n")
while True:
    user_input = input("Guess the number: \n")
    
    if user_input == "exit":
        print("CLOSED ❌❌❌")
        break

    attempts += 1
    user_guess = int(user_input)
    if(number == user_guess):
        print("CORRECT✅✅✅")
        break
    elif user_guess < (number - 5):
        print("Too low...\n")
    elif user_guess > (number + 5):
        print("Too high...\n")
    else:
        print("Keep guessing...\n")

print(f"\nYou took {attempts} attempt(s) to guess the number")