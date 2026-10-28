def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error: Please enter a valid integer.")
            print("Please try again.")


num1 = get_valid_int("Enter the first number: ")
num2 = get_valid_int("Enter the second number: ")

addition = num1 + num2
subtraction = num1 - num2

print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")