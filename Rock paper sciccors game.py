import random

choices = ["rock", "paper", "scissors"]

print("Welcome to Rock, Paper, Scissors!")
print("Type rock, paper, or scissors. Type q to quit.\n")

while True:
    user_choice = input("Your choice: ").strip().lower()

    if user_choice == "q":
        print("Thanks for playing!")
        break

    if user_choice not in choices:
        print("Invalid choice, try again.")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!\n")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!\n")
    else:
        print("You lose!\n")
