#Calculator

def add(n1, n2): #adds n1 and n2
    return n1 + n2
def subtract(n1, n2): #subtracts n1 and n2
    return n1 - n2
def multiply(n1, n2): #multiplies n1 and n2
    return n1 * n2
def divide(n1, n2): #divides n1 and n2
    return n1 / n2


n1 = int(input("Enter the first number: "))
ask = input("Choose an operatos: +, -, * or /.")
n2 = int(input("Enter the fsecond number: "))

dic = {
    "+": add(n1, n2),
    "-": subtract(n1, n2),
    "*": multiply(n1, n2),
    "/": divide(n1, n2),
}
if ask == "+":
    print(add(n1, n2))
elif ask == "-":
    print(subtract(n1, n2))
elif ask == "*":
    print(multiply(n1, n2))
elif ask == "/":
    print(divie(n1, n2))