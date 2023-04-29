# import module
import random
import art

def replace_ace(list):
    while sum(list) > 21 and 11 in list:
       ace_index = list.index(11)
       list[ace_index] = 1
    return list

def play_black_jack():
    
    wanna_play = input("Do you want to play a game of BlackJack? Type 'y' or 'n'\n").lower()

    if wanna_play == 'y':
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

        your_card = random.sample(cards, 2)

        computer_card = random.choice(cards)

        print(art.logo)
        print(f"Your cards: {your_card}, current score: {sum(your_card)} ")

        print(f"Computer's first card: {computer_card}")

        while sum(your_card) < 21:

            wanna_pick_another_card = input("Type 'y' to get another card, type 'n' to pass:\n").lower()

            if wanna_pick_another_card == 'y':
                your_card.append(random.choice(cards))

            if sum(your_card) > 21:
                your_card = replace_ace(your_card)

            print(f"Your cards: {your_card}, current score: {sum(your_card)} ")    
        
        computer_cards = [computer_card]
        
        while sum(computer_cards) < 16: 

            computer_cards.append(random.choice(cards))

            if sum(computer_cards) > 21:
                computer_cards = replace_ace(computer_cards)

        print(f"Your cards: {your_card}, current score: {sum(your_card)} ")

        print(f"Computer's cards: {computer_cards}, current score: {sum(computer_cards)} ")

        if sum(your_card) > 21:
            print("You went over. You Lose !!!")
        elif sum(computer_cards) > 21:
            print("CPU went over. You WON !!!")
        elif sum(your_card) == sum(computer_cards):
            print("Its a Draw")
        elif sum(your_card) > sum(computer_cards):
            print("You Won !!!")
        else:
            print("You Lose!!")

        play_black_jack()
    else:
        return




play_black_jack()