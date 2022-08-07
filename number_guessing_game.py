import random
import art

EASY_LEVEL = 10
HARD_LEVEL = 5

# set a difficulty level
def difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard'. ")
    if level == 'easy':
        return EASY_LEVEL
    else:
        return HARD_LEVEL

# function to check user's guess against actual number.
def check_user_guess(guess_number, answer, turns):
    """Check answer against the guess. Return the number of turns remaining."""
    if guess_number == answer:
        print(f"You got it! The answer was {answer}.")
    elif guess_number < answer:
        print("Too low.")
        return turns - 1
    elif guess_number > answer:
        print("Too high.")
        return turns - 1

def play_game():
    print(art.logo)
    # choosing a random number between 1 and 100.
    print("Welcome to number guessing game.")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    # print(f"Psst, the correct answer is {answer}.")
    # let the user guess the number
    turns = difficulty()

    # Repeat the guessing functionality if they get wrong.
    guess_number = 0
    while guess_number != answer:
        print(f"You have {turns} attempts remaining to guessing the game.")
        guess_number = int(input("Make a Guess: "))
        turns = check_user_guess(guess_number, answer, turns)
        if turns == 0:
            print("You're ran out of guesses, you lose.")
            return
        elif guess_number != answer:
            print("Guess Again.")
    # track the number of turns and reduced by one.
play_game()