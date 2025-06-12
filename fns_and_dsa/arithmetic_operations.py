def perform_operation(num1, num2, operation):
    num1 = float(num1)
    num2 = float(num2)
    match operation :
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if(num2 == 0):
                print('You cannot divide by 0')
                return None
            return num1 / num2