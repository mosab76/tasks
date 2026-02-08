def calculator(a, operation, b):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operation"

x = float(input("Enter first number: "))
op = input("Enter operation (+, -, *, /): ")
y = float(input("Enter second number: "))
result = calculator(x, op, y)
print("Result:", result)
