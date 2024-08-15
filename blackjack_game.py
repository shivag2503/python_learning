import random

print("Welcome to the Blackjack game....")


def random_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    total_of_cards = sum(cards)
    if total_of_cards == 21 and len(cards) == 2:
        return 0
    elif total_of_cards > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        return sum(cards)
    else:
        return total_of_cards


def compare(p_score, d_score):
    if p_score == d_score:
        print("Draw...")
    elif d_score == 0:
        print("Your opponent has blackjack. You lost...")
    elif p_score == 0:
        print("You have blackjack. You win...")
    elif p_score > 21:
        print("You went out. You lost...")
    elif d_score > 21:
        print("Your opponent went out. You win...")
    elif p_score < d_score:
        print("You lost...")
    else:
        print("You win...")


def blackjack():
    dealer = []
    player = []
    dealer_score = -1
    player_score = -1
    is_game_over = False

    for i in range(1, 3):
        dealer.append(random_card())
        player.append(random_card())

    while not is_game_over:
        player_score = calculate_score(player)
        dealer_score = calculate_score(dealer)

        print(f"Your cards: {player}, current score: {player_score}")
        print(f"Computer's first card: {dealer[0]}")

        if dealer_score == 0 or player_score == 0 or player_score > 21:
            is_game_over = True
        else:
            y_n = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if y_n == 'y':
                player.append(random_card())
            else:
                is_game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer.append(random_card())
        dealer_score = calculate_score(dealer)

    print(f"Your final hand: {player}, current score: {player_score}")
    print(f"Computer's final hand: {dealer}, current score: {dealer_score}")

    compare(player_score, dealer_score)


cont_game = True
while cont_game:
    y_n = input("Do you want to play a game of blackjack? Type 'y' or 'n': ").lower()
    if y_n == "y":
        print("\n" * 20)
        blackjack()
    else:
        exit(0)