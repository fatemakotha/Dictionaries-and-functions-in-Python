#Print statement after Return statement
def my_function(a):
    if a < 40:
        return
        print("Terrible")
    if a < 80:
        return "Pass"
    else:
        return "Great"
print(my_function(25))

#prints: None
# The return keyword will exit the function and prevent the rest of the code from being executed.