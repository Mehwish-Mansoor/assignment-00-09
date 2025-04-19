def print_ones_digit(num):
    """
    Prints the ones digit of the given number.
    """
    ones_digit = num % 10  # Get the ones digit using the modulo operator
    print(f"The ones digit is {ones_digit}")

def main():
    # Prompt the user to enter a number
    num = int(input("Enter a number: "))
    
    # Call the print_ones_digit function
    print_ones_digit(num)

if __name__ == '__main__':
    main()