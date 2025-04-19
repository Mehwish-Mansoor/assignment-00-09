import random

DONE_LIKELIHOOD = 0.3  # Likelihood of being done at each step

def done():
    """
    Returns True with likelihood DONE_LIKELIHOOD.
    """
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    """
    Prints numbers from 1 to 10, but stops early if done() returns True.
    """
    for i in range(1, 11):  # Loop from 1 to 10
        if done():  # Check if done() returns True
            return  # Exit the function early
        print(i, end=" ")  # Print the current number

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("\nI'm done.")

if __name__ == '__main__':
    main()