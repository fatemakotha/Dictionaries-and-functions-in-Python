# Accept a list of 5 float numbers as an input from the user

list = []

def make_list():
    for _ in range(0, 5):
        number = float(input("Enter integer: "))
        list.append(number)
    print(list)
make_list()
#prints:
# Enter integer: 2.3
# Enter integer: 2.3
# Enter integer: 3.6
# Enter integer: 3.5
# Enter integer: 3.2
# [2.3, 2.3, 3.6, 3.5, 3.2]