#Calculator

def add(n1, n2): #adds n1 and n2
    return n1 + n2
def subtract(n1, n2): #subtracts n1 and n2
    return n1 - n2
def multiply(n1, n2): #multiplies n1 and n2
    return n1 * n2
def divide(n1, n2): #divides n1 and n2
    return n1 / n2

from replit import clear


def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer #if yes, then the answer of the first calculation is set to num1 and num2 is for user to enter
    else:
      should_continue = False
      clear()
      calculator()

calculator()