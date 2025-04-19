import random

# Initialize scores and number of rounds
player_score = 0
rounds = 5  # You can adjust the number of rounds

print("Welcome to the High-Low game!")

# Play the game for the specified number of rounds
for round_num in range(1, rounds + 1):
    print(f"\nRound {round_num}:")
    
    # Generate random numbers for player and computer
    player_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)
    
    print(f"Your number is: {player_number}")
    
    # Ask the player to guess
    guess = input("Do you think your number is higher or lower than the computer's? (Enter 'higher' or 'lower'): ").strip().lower()
    
    # Determine the result
    if (guess == "higher" and player_number > computer_number) or (guess == "lower" and player_number < computer_number):
        print(f"Correct! The computer's number was {computer_number}.")
        player_score += 1
    else:
        print(f"Wrong! The computer's number was {computer_number}.")
    
# Display the final score
print(f"\nGame over! Your final score is: {player_score}/{rounds}")