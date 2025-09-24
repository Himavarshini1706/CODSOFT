import random
import json
import os

SCORE_FILE = "rps_scores.json"

# Load leaderboard scores
def load_scores():
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, "r") as f:
            return json.load(f)
    return {"user": 0, "computer": 0, "ties": 0, "games_played": 0}

# Save scores to file
def save_scores(scores):
    with open(SCORE_FILE, "w") as f:
        json.dump(scores, f, indent=4)

# Computer AI: sometimes counters the user's last move
def get_computer_choice(last_user_choice=None):
    choices = ["rock", "paper", "scissors"]
    if last_user_choice:
        # Computer has a 40% chance to counter your last move
        counter_moves = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
        if random.random() < 0.4:
            return counter_moves[last_user_choice]
    return random.choice(choices)

def get_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def play_round(scores, last_user_choice=None):
    user_choice = input("\nEnter your choice (rock/paper/scissors or exit): ").lower()

    if user_choice == "exit":
        return None, None

    if user_choice not in ["rock", "paper", "scissors"]:
        print("⚠️ Invalid choice! Please enter rock, paper, or scissors.")
        return None, last_user_choice

    computer_choice = get_computer_choice(last_user_choice)
    print(f"🤖 Computer chose: {computer_choice}")

    winner = get_winner(user_choice, computer_choice)

    if winner == "tie":
        print("😐 It's a tie!")
        scores["ties"] += 1
    elif winner == "user":
        print("🎉 You win this round!")
        scores["user"] += 1
    else:
        print("💻 Computer wins this round!")
        scores["computer"] += 1

    scores["games_played"] += 1
    save_scores(scores)

    print(f"🏆 Current Score → You: {scores['user']} | Computer: {scores['computer']} | Ties: {scores['ties']}")
    return winner, user_choice

def best_of_mode(scores):
    try:
        rounds = int(input("How many rounds? (e.g., 3, 5, 7): "))
        if rounds % 2 == 0:
            print("⚠️ Please enter an odd number for a proper best-of match.")
            return
    except ValueError:
        print("⚠️ Invalid input.")
        return

    user_wins = computer_wins = 0
    needed = rounds // 2 + 1
    last_user_choice = None

    print(f"\n🎮 Starting best of {rounds} match! First to {needed} wins.")

    while user_wins < needed and computer_wins < needed:
        winner, last_user_choice = play_round(scores, last_user_choice)
        if winner == "user":
            user_wins += 1
        elif winner == "computer":
            computer_wins += 1

    if user_wins > computer_wins:
        print(f"\n🎉 You won the best of {rounds} match! Final Score: {user_wins} - {computer_wins}")
    else:
        print(f"\n💻 Computer won the best of {rounds} match! Final Score: {computer_wins} - {user_wins}")

def view_statistics(scores):
    print("\n📊 Game Statistics:")
    print(f"Total games played: {scores['games_played']}")
    print(f"You won: {scores['user']} times")
    print(f"Computer won: {scores['computer']} times")
    print(f"Ties: {scores['ties']}")

def main():
    scores = load_scores()

    while True:
        print("\n=== Rock-Paper-Scissors Menu ===")
        print("1. Play Single Round")
        print("2. Play Best of N Rounds")
        print("3. View Statistics")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            play_round(scores)
        elif choice == "2":
            best_of_mode(scores)
        elif choice == "3":
            view_statistics(scores)
        elif choice == "4":
            print("\n👋 Thanks for playing! Come back soon!")
            break
        else:
            print("⚠️ Invalid option. Try again.")

if __name__ == "__main__":
    main()