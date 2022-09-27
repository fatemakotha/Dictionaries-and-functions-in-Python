#Write a program to create function func1() to accept a variable length of arguments and print their value as a list.

def make_list(a, b, c):
    list = [a, b, c]
    print(list)


a = input("Enter a: ")
b = input("Enter b: ")
c = input("Enter c: ")
make_list(a, b, c)