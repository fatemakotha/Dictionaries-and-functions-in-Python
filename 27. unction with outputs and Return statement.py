#Function with outputs and Return statement
def title():
    first = input("Enter first name: ")
    last = input("Enter last name: ")
    
    x = first.title()
    y = last.title()
    fullname = x + y
    return fullname
    

print(title())