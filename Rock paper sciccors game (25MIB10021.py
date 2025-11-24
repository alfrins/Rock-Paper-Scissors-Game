import random
#used to import random module in oredr to generate randomness between rock,paper and scissors

a = ["rock", "paper", "scissors"] #list formed to choose between options

print("Welcome to Rock, Paper, Scissors!")
print("Type rock, paper, or scissors. Type q to quit.\n")
#initialisiong while loop to check wether the user want to continue the game or not
while True:
    b = input("Your choice: ").strip().lower()
    #optionthat is required to quit
    if b== "q":
        print("Thanks for playing!")
        break
    #option provided in order to prevent the user from inputting wrong choices
    if b not in a:
        print("Invalid choice, try again.")
        continue
    #random used
    c= random.choice(a)
    print(f"Computer chose: {c}")
    #to check if the point is draw. that is both computer and user have the same choice
    if b == c:
        print("It's a tie!\n")
    elif (
        (b == "rock" and c == "scissors") or
        (b == "paper" and c == "rock") or
        (b == "scissors" and c == "paper")
    ):
        print("You win!\n")# printing that the user has won
    else:
        print("You lose!\n")#printing that the user has lost
