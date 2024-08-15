def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def perform_calc(op, num1, num2):
    return operations[op](num1, num2)


def calculator():
    flag = True
    num_1 = float(input("Please enter the first number: "))

    while flag:
        operator = input(f"Please enter the mathematical operator from below: \n+\n-\n*\n/\n")
        num_2 = float(input("Please enter the second number: "))
        result = perform_calc(operator, num_1, num_2)
        print(f"{num_1} {operator} {num_2} = {result}")

        yes_no = (input(
            f"Do you want to continue the next operation with this {result} or start with fresh? Type 'yes' or 'no': ")
                  .lower())

        if yes_no == "yes":
            num_1 = result
        else:
            flag = False
            print("\n"*25)
            calculator()


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

calculator()
