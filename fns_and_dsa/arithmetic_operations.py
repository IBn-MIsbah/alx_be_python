def perform_operation(num1: float, num2:float, operation: str):
    match operation :
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            return "Error: Division by zero is not allowed" if num2 == 0 else num1 / num2
        case _:
            return "Error: Invalid operation"