import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

number = round(random.uniform(0, 1) * 100)
easy_life = 10
hard_life = 5

level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()


def result(guess, life):
    if guess < number:
        print("Too low.\nGuess again.")
        return life - 1
    elif guess > number:
        print("Too high.\nGuess again.")
        return life - 1
    else:
        print("You win")
        exit(0)


def game(life):
    number_guessed = int(input("Make a guess: "))
    return result(number_guessed, life)


flag = True
while flag:
    if level == "easy":
        print(f"Yoy have {easy_life} attempts remaining to guess the number.")
        easy_life = game(easy_life)
        print(f"easy life {easy_life}")
        if easy_life < 1:
            print("No attempts left. You lost")
            flag = False
    else:
        print(f"Yoy have {hard_life} attempts remaining to guess the number.")
        hard_life = game(hard_life)
        if hard_life < 1:
            print("No attempts left. You lost")
            flag = False






