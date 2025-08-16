import random

# Track the number of rounds and total guesses across the entire game.
rounds_played = 0
total_guesses = 0

print("Welcome to the Unending Guessing Game!")
print("Guess the secret number to win the round. Type 'quit' to end the game.")

# Create a loop that will run indefinitely until the user decides to quit.
# Hint: what Boolean will make something always run 🤔🤔🤔
while ____________________:
    # Get a new random secret number for this round.
    secret_number = random.randint(1, 10)

    # Track guesses for the current round.
    guesses_this_round = 0
    rounds_played = rounds_played + 1

    print(f"\n--- Round {rounds_played} ---")

    # Create a nested loop for the actual guessing.
    # The loop should continue until the user guesses correctly.
    while ______________________:
        user_input = input("Enter your guess: ") ## ⚠️notice that we're not limiting the user input to Numbers!!!!!!

        # TODO: Add an if/elif/else block here.
        # 1. If the user enters 'quit', break out of BOTH loops.
        #    HINT: Use a flag variable or a nested break for this.
        # 2. If the user enters a number, convert it to an integer.
        # 3. If the guess is correct, print a win message, add to total_guesses, and break out of the inner loop.
        # 4. If the guess is wrong, tell the user if it's too high or too low, and increment guesses_this_round.

        if _____________________:
            print("Thanks for playing!")
            break

        try:
            guess = int(user_input)
            guesses_this_round = guesses_this_round + 1
            if ____________________:
                print("You got it!")
                total_guesses = total_guesses + guesses_this_round
                break
            elif ____________________:
                print("Too high!")
            else:
                print("Too low!")
        except ValueError:
            print("Invalid input. Please enter a number or 'quit'.")

    # HINT: What happens if the user quits? We need to make sure the outer loop also ends.
    # A simple 'if' check after the inner loop is one way to do it.

# TODO: After the outer loop, calculate and print the average number of guesses.
# HINT: Check if rounds_played is greater than 0 to avoid a division-by-zero error.
#
# if __________________:
#     average_guesses = ______________________
#     print(f"Game over! You played {rounds_played} rounds.")
#     print(f"On average, it took you {average_guesses:.2f} guesses per round.")
# else:
#     print("No rounds were played. Goodbye!")
