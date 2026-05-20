import random
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

get_another_card = True

def check_score(user_score,dealer_score,user_card_list,get_another_card,dealer_card_list):
    if user_score > 21:
        if 11 in user_card_list:
            user_score = user_score - 10
            if user_score > 21:
                print("It's a bust. You lose!")
                return blackjack()

        else:
            if user_score > 21:
                print("It's a bust. You lose!")
                return blackjack()


    else:
        while get_another_card:
            get_another = input("Type 'y' to get another card, type 'n' to pass:").lower()

            if get_another == "y":
                user_card_list.append(random.choice(cards))
                user_score = sum(user_card_list)
                dealer_card_list.append(random.choice(cards))
                dealer_score = sum(dealer_card_list)
                print(f"Your cards: {user_card_list}, current score: {user_score}")
                print(f" Computer's first card: {dealer_card_list[0]}")
                return check_score(user_score, dealer_score, user_card_list, get_another_card, dealer_card_list)

            else:
                print(f"Your final hand: {user_card_list}, final score: {user_score}")
                print(f"Computer's final hand: {dealer_card_list}, final score: {dealer_score}")
                if user_score > dealer_score and user_score <=21:
                    print("You Win!")
                    blackjack()

                elif user_score < dealer_score and dealer_score <= 21:
                    print("Computer Wins!")
                    blackjack()

                elif user_score < dealer_score and dealer_score > 21:
                    print("Computer got a bust. You Win!")
                    blackjack()

                else:
                    print("It's a Draw")
                get_another_card = False
                return blackjack()



def blackjack():
    dealer_score = 0
    user_score = 0
    global get_another_card
    dealer_card_list = []
    user_card_list = []
    black_jack_user = False
    black_jack_dealer = False

    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()
    if play == 'y':

        user_card_list = random.sample(cards,2)
        dealer_card_list = random.sample(cards,2)

        user_score = sum(user_card_list)
        dealer_score = sum(dealer_card_list)

        if 11 in user_card_list and user_score == 21:
            black_jack_user = True

        if 11 in dealer_card_list and dealer_score == 21:
            black_jack_dealer = True

        print(f"Your cards: {user_card_list}, current score: {user_score}")

        print(f" Computer's first card: {dealer_card_list[0]}")

        if black_jack_dealer or black_jack_user:

            if black_jack_dealer:
                print("Computer has BlackJack it Wins!")
            elif black_jack_user:
                print("You got BlackJack You Won!")
            return
        else:
            check_score(user_score,dealer_score,user_card_list,get_another_card,dealer_card_list)

    else:
        return

print(logo)
blackjack()

