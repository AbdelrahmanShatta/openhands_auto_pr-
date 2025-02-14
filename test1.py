"""
A simple program to add two numbers with input validation.

The program repeatedly prompts the user for input until valid integers are provided,
then calculates and displays their sum.
"""


def get_number(prompt):
    """Prompt the user for an integer input, validating the input before inseration."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def main():
    """Main function to get two numbers from the user and print their sum."""
    x = get_number("Input the first number: ")
    y = get_number("Input the second number: ")
    print(f"The sum is: {x + y}")


if __name__ == "__main__":
    main()
