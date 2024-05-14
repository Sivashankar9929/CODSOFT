import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def print_scores(user_score, computer_score):
    print(f"Your score: {user_score}, Computer's score: {computer_score}")

def play_again():
    choice = input("Do you want to play again? (yes/no): ")
    return choice.lower() == 'yes'

def main():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors Game!")

    while True:
        print("\nChoose: rock, paper, or scissors.")
        user_choice = input("Your choice: ").lower()

        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print("Computer's choice:", computer_choice)

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        print_scores(user_score, computer_score)

        if not play_again():
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
