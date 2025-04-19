def is_odd(num):
    """
    Returns True if the number is odd, False otherwise.
    """
    return num % 2 != 0

def main():
    # Loop through numbers from 10 to 19
    for num in range(10, 50):
        if is_odd(num):
            print(f"{num} odd")
        else:
            print(f"{num} even")

if __name__ == '__main__':
    main()