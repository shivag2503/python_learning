import random

print("USER")

user_choice = int(input("Enter 0 for ROCK, 1 for PAPER, 2 for SCISSOR. Your choice: "))

print(user_choice)

if user_choice == 0:
    print("ROCK")
elif user_choice == 1:
    print("PAPER")
elif user_choice == 2:
    print("SCISSOR")
else:
    print("Wrong choice!!")
    exit(0)

print("\n")
print("#######################################################")
print("\n")

print("COMPUTER")

computer_choice = random.randint(0, 2)

print("Computer selected:")

if computer_choice == 0:
    print("ROCK")
elif computer_choice == 1:
    print("PAPER")
else:
    print("SCISSOR")

if user_choice == computer_choice:
    print("DRAW")
elif ((user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or
      (user_choice == 2 and computer_choice == 1)):
    print("YOU WIN")
else:
    print("YOU LOST")
