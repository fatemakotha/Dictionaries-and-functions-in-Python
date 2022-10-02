from random import randint
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def set_difficulty():
    level = input("Enter a difficulty level: 'easy' or 'hard'!!!")
    if level == "easy":
        return EASY_LEVEL_TURNS #returns 10
    else:
        return HARD_LEVEL_TURNS #returns 5


def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")
    


def game():
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    #Choosing a random number between 1 and 100.
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}") 
    
    turns = set_difficulty() #turns set to 10 or 5
    should_continue = True
    guess = 0
    while should_continue:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns) #You got it! The answer was 6.
        if turns == 0:
            print("You've run out of guesses, you lose.")
            should_continue = False
        elif guess == answer:
            should_continue = False
        elif guess != answer:
            print("Guess Again")

game()
