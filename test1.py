def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    x = get_number("Input the first number: ")
    y = get_number("Input the second number: ")
    print(f"The sum is: {x + y}")

if __name__ == "__main__":
    main()
