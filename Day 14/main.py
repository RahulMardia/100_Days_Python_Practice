import art
from game_data import data
import random



def high_low():
    player_right = False
    keep_playing = True
    len_dict = len(data)
    score = 0
    print(art.logo)

    while keep_playing :
        if not player_right :
            random_a, random_b = random.sample(range(len_dict), 2)
        print(f"Compare A: {data[random_a]['name']}, a {data[random_a]['description']}, from {data[random_a]['country']}.")
        print(art.vs)
        print(f"Compare B: {data[random_b]['name']}, a {data[random_b]['description']}, from {data[random_b]['country']}.")

        choice = input("Who has more followers? Type 'A' or 'B':").lower()

        player_choose = random_a if choice == 'a' else random_b
        computer_choose = random_a if choice == 'b' else random_b

        if data[player_choose]['follower_count'] > data[computer_choose]['follower_count']:
            score += 1
            print(f"You're right! Current score: {score}.")
            player_right = True
            keep_playing = True

            random_a = random_b
            random_b = random.randint(0, len_dict - 1)

        else:
            print("\n" * 20)
            print(f"Sorry, that's wrong. Final score: {score}")
            keep_playing = False


high_low()