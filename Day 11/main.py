# import module
import random
import art

def cards():
    return [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def calculate_score(list):
    total_score = sum(list)
    # if first 2 card has 11 and 10 then its a Black Jack
    if total_score == 21 and len(list) == 2:
        return 0
    # replace 11 with 1 if score is greater then 21
    elif total_score > 21 and 11 in list:
        list.remove(11)
        list.append(1)
    
    return sum(list)

def pick_cards(count):
    # return list of random cards
    return random.sample(cards(), count)

def compare_score(user_score, computer_score):
    if computer_score == user_score:
        return "Its a Draw"
    elif computer_score == 0:
        return "Computer WON .. BlackJack"
    elif user_score == 0:
        return "You Won ... BlackJack"
    elif user_score > 21:
        return "You Lose .. its Bust"
    elif computer_score > 21:
        return "You Won ... Computer Bust"
    elif user_score > computer_score:
        return "You Won"
    else:
        return "You Lose" 
    
def is_game_over(calculated_user_score, calculate_computer_score):
    return calculated_user_score == 0 or calculate_computer_score == 0 or calculated_user_score > 21

def play_game():

    print(art.logo)

    user_cards = pick_cards(2)
    computer_cards = pick_cards(2)

    print(f"Your cards: {user_cards}, current score: {sum(user_cards)} ")
    print(f"Computer's first hand: {computer_cards[0]}")    
    
    calculated_user_score = calculate_score(user_cards)
    calculate_computer_score = calculate_score(computer_cards)

    has_ended = is_game_over(calculated_user_score,calculate_computer_score)

    while not has_ended:

       if input("Type 'y' to get another card, type 'n' to pass:\n").lower() == 'y':
           user_cards.extend(pick_cards(1))
           calculated_user_score = calculate_score(user_cards)
           has_ended = is_game_over(calculated_user_score,calculate_computer_score)
       else:
           has_ended = True     
        
       print(f"Your cards: {user_cards}, current score: {calculated_user_score} ")

    calculated_user_score = calculate_score(user_cards)

    if calculate_computer_score < 17:
        computer_cards.extend(pick_cards(1))
        calculate_computer_score = calculate_score(computer_cards)

    print(f"Your final cards: {user_cards}, final score: {calculated_user_score}.")
    print(f"Computer's cards: {computer_cards}, final score: {calculate_computer_score}.")

    print(compare_score(user_score=calculated_user_score, computer_score=calculate_computer_score))

while input("Do you want to play a game of BlackJack? Type 'y' or 'n'\n").lower() == 'y':
    play_game()