# import modules
import random

# import files
import stages
import word_list 


print(stages.logo)

# random words to pick hangman
world_list = word_list.word_list

# TODO: choose a random word
chosen_one = random.choice(world_list)

# TODO: create a blank options same as chosen words

guess_list = []

is_hang_man_saved = False

you_have_total_life = 7

def print_hangman():

    global is_hang_man_saved
    
    hangman = ''

    for word in chosen_one:        
        # Check if guess list contains the guess
        if guess_list.__contains__(word):
            hangman += f' {word}'
        
        # print blank otherwise
        else:   
             hangman += ' _'
    
    if not is_hang_man_saved :
        is_hang_man_saved = hangman.replace(" ", "") == chosen_one

    print(f"{hangman}\n")


print_hangman()

# TODO : ask a user to guess a letter and assign 
# their answer to a variable classed guess. with lowercase

while not is_hang_man_saved and you_have_total_life > 0:

    guess = input("Guess a latter and save the hangman... \n").lower()

    if guess in guess_list:
        print("You have already chosen this word !!! \n")
    elif guess in chosen_one:
        guess_list.append(guess)
        print("Its a match !!")
        print_hangman()
    else:
        you_have_total_life -= 1
        print(stages.stages[you_have_total_life])


if is_hang_man_saved:
    print("You HAVE SAVED A LIFE !!")
else:
    print("YOU HAVE FAILED !!")