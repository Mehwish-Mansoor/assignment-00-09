import random  # Import the random module to generate random numbers

def main():
    # Simulate rolling two dice
    die1 = random.randint(1, 6)  # Roll the first die (random number between 1 and 6)
    die2 = random.randint(1, 6)  # Roll the second die (random number between 1 and 6)
    
    # Calculate the total
    total = die1 + die2
    
    # Print the results
    print(f"Die 1: {die1}")
    print(f"Die 2: {die2}")
    print(f"Total: {total}")

if __name__ == '__main__':
    main()