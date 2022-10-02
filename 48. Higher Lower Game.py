import random

print("Welcome to the Guessing GAME!")
print("I am thinking of a number between 1 - 100.")

number = random.randint(1, 100)
print(f"The chosen number is {number}")

lives = 0
should_continue = True

choice = input("Choose a difficulty level, 'easy' or 'hard'.")
               
if choice == "easy":
    lives = 10
    print(lives)
else:
    lives = 5


while should_continue:
    guess = int(input("Guess a number: "))

    if guess > number:
        lives -= 1
        print(f"You have {lives} left")
        print("Too High")
    elif guess < number:
        lives -= 1
        print(f"You have {lives} left")
        print("Too low")
    elif guess == number:
        should_continue = False
        print("You win")
    if lives == 0:
        should_continue = False
        print("Game over")