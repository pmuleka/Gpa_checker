Prisca Muleka 3/225/2024
""" This program prompts the user for two floating-point numbers, adds them together, and outputs the result to the console. """

def main():
    # Prompt the user for the first floating-point number
    num1 = float(input("Enter the first floating-point number: "))

    # Prompt the user for the second floating-point number
    num2 = float(input("Enter the second floating-point number: "))

    # Add the two numbers together
    result = num1 + num2

    # Output the result to the console
    print("The sum of", num1, "and", num2, "is:", result)

if __name__ == "__main__":
    main()
