from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calc = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    """This function calculates the answer."""
    print(logo)
    continue_operation = True

    num1 = int(input("Enter first number: "))
    while continue_operation:
        operation = input(f"Enter operation [Choice: {", ".join(calc.keys())}]: ")
        num2 = int(input("Enter second number: "))
        answer = calc[operation](n1=num1, n2=num2)
        print(f"{num1} {operation} {num2} = {answer}")
        choice = input(f"Type 'y' to continue calculation with {answer}, or type 'n' to start a new calculation.").lower()

        if choice == "y":
            num1 = answer
        else:
            continue_operation = False
            print("\n" * 20)
            calculator()

calculator()
