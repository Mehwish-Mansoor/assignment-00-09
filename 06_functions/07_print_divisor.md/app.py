def print_divisors(num):
    """
    Prints all divisors of the given number.
    """
    for i in range(1, num + 1):  # Loop from 1 to num (inclusive)
        if num % i == 0:  # Check if i is a divisor of num
            print(i, end=" ")  # Print the divisor on the same line

def main():
    # Ask the user for a number
    num = int(input("Enter a number: "))
    print(f"Here are the divisors of {num}")
    print_divisors(num)  # Call the helper function

if __name__ == '__main__':
    main()