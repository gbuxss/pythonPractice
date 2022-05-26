# Write a program to perform simple calculation

def user_input():
    first_number = float(input("enter first number:\t"))
    second_number = float(input("enter second number:\t"))
    operation = input("Choose operation from list:\n Add \n Sub \n Mul \n Div\n Exit\n").lower()

    def perform_add(num1, num2):
        return num1 + num2

    def perform_sub(num1, num2):
        return num1 - num2

    def perform_mul(num1, num2):
        return num1 * num2

    def perform_div(num1, num2):
        return num1 / num2

    if operation == "Add".lower():
        print(perform_add(first_number, second_number))
    elif operation == "Sub".lower():
        print(perform_sub(first_number, second_number))
    elif operation == "Mul".lower():
        print(perform_mul(first_number, second_number))
    elif operation == "Div".lower():
        print(perform_div(first_number, second_number))
    elif operation == "Exit".lower():
        break
    else:
        print("Wrong operation entered")




user_input()
