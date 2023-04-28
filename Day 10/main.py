number_1 = int(input("Please select first number to calculate \n"))

number_2 = int(input("Please select second number to calculate \n"))

operator = input("Please select the operator / * + - \n")

def calculator(num1, num2, operator):
    
    if operator == '/':
        return num1 / num2
    elif operator == '*':
        return num1 * num2
    elif operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    else:
        return "Invalid Operation"

result = calculator(num1=number_1, num2=number_2,operator=operator)

print(result)