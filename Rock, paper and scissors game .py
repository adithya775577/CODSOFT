import random

choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0

while True:
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    computer_choice = random.choice(choices)

    print(f"User's choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break

print(f"Final Scores - User: {user_score}, Computer: {computer_score}")