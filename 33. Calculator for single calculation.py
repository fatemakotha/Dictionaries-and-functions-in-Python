#Calculator

def add(n1, n2): #adds n1 and n2
    return n1 + n2
def subtract(n1, n2): #subtracts n1 and n2
    return n1 - n2
def multiply(n1, n2): #multiplies n1 and n2
    return n1 * n2
def divide(n1, n2): #divides n1 and n2
    return n1 / n2


operations = {
    "+": add, #add is the name of the function addition which is set to the value here
    "-": subtract, #subtract is the name of the function addition which is set to the value here
    "*": multiply, #multiply is the name of the function addition which is set to the value here
    "/": divide, #divide is the name of the function addition which is set to the value here
}

num1 = int(input("Enter the first number: "))
for symbol in operations:
    print(symbol)
operator = input("Choose an operator: +, -, * or /.")
num2 = int(input("Enter the fsecond number: "))

calculation_function = operations[operator] 
#calculation_function = operations["+"]
#calculation_function = add
answer = calculation_function(num1, num2)
# answer = add(num1, num2)
print(f"{num1} {operator} {num2} = {answer}")