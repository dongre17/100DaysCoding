# import modules
import random

MAGIC_NUMBER = random.randint(1, 100)

def difficulty_attempts():

    difficulty_level = input("Choose a difficulty level. Type 'easy' or 'hard'\n")

    if difficulty_level == 'easy':
        return 10
    elif difficulty_level == 'hard':
        return 5
    
    return 0

def play_number_guess(number_of_attempts):
    
    is_end_of_game = False

    while number_of_attempts > 0 and not is_end_of_game:

        print(f"You have {number_of_attempts} attempts remaining to guess the number.")

        guess_number = int(input("Make a Guess:"))

        if guess_number == MAGIC_NUMBER:
            is_end_of_game = True
        elif guess_number > MAGIC_NUMBER:
            print("Too High!!")
        elif guess_number < MAGIC_NUMBER:
            print("Too Low!!")

        number_of_attempts -= 1

    if is_end_of_game:
        print(f"Great You Won the game and {number_of_attempts} attempts remaining ")
    else:
        print("You have failed")


print("Welcome to the Number Guess Game!")

print("I am thinking of a number between 1 and 100")

play_number_guess(difficulty_attempts())

