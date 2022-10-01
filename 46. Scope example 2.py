# What will be printed in the console when the code is run?

i = 50
def foo():
    i = 100
    return i
 
foo()
print(i)
#prints: 50
# The print statement is outside the function foo(). So it can't access the local variable i = 100. It only sees the global i, which is equal to 50.