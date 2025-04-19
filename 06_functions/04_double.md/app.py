def double(num):
    """
    Returns the result of multiplying num by 2.
    """
    return num * 2

def main():
    # Ask the user for a number
    num = int(input("Enter a number: "))
    
    # Call the double function and print the result
    result = double(num)
    print(f"Double that is {result}")

if __name__ == '__main__':
    main()