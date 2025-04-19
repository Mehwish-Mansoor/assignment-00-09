def print_multiple(message, repeats):
    """
    Prints the given message a specified number of times.
    """
    for _ in range(repeats):  # Loop repeats times
        print(message, end=" ")  # Print the message on the same line

def main():
    # Prompt the user for a message and the number of repeats
    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    
    # Call the print_multiple function
    print_multiple(message, repeats)

if __name__ == '__main__':
    main()