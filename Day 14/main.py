# import module
import random
import art
import game_data

final_score = 0
is_game_end = False

player_one = random.choice(game_data.data)

# Run till game end
while not is_game_end:
    # is player 2 is not defined then choose from the list 
    if player_one is None:
        player_one = player_two
        
    player_two = random.choice([x for x in game_data.data if x != player_one])

    print(art.logo)
    
    print(f"Compare A: {player_one['name']}, {player_one['description']}, from {player_one['country']}")

    print(art.vs)

    print(f"Compare B: {player_two['name']}, {player_two['description']}, from {player_two['country']}")

    pick_more_famous_celebrity = input("Who has more followers? Type 'A' or 'B' ").upper()

    who_is_more_famous = ''

    if player_one['follower_count'] > player_two['follower_count']:
        who_is_more_famous = 'A'
    else:
        who_is_more_famous = 'B'
        player_one = None
    
    if who_is_more_famous == pick_more_famous_celebrity:
        final_score += 1        
    else:
        is_game_end = True


print(f"Your final score is {final_score}")