import random

word_list = ["apple", "mouse", "rainbow"]

chosen_word = random.choice(word_list)

placeholder = ""

for i in chosen_word:
    placeholder += "_"

print("Welcome to the Hangman Game. You have to guess the correct word and you have only 6 chances else ur game is "
      "over.")

print(f"Your word is: {placeholder}")

correct_letters = []
wrong_letters = []

game_over = False
life = 6

while not game_over:
    if life < 1:
        print("Sorry you loss the game!!!")
        game_over = True
    else:
        guess = input("Please guess a letter...").lower()
        if guess in correct_letters:
            print("You already chose the letter and its contain in the word. Choose next.")

        display = ""
        for letter in chosen_word:
            if letter == guess:
                display += letter
                correct_letters.append(guess)
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"

        if guess not in chosen_word:
            life -= 1

        print(display)

        if "_" not in display:
            print("Cool!! You win")
            game_over = True
