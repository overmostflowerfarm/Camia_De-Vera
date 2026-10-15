# Global variables vvvvv
num1 = input("Enter your first number: ")
num2 = input("Enter your second number: ")
def calculate_sum():
    # Local variables vvvvv
    sum = float(num1) + float(num2)
    print(f"Sum: {sum}")
def calculate_diff():
    # Local variables vvvvv
    difference = float(num1) - float(num2)
    print(f"Difference: {difference}")
calculate_sum()
calculate_diff()