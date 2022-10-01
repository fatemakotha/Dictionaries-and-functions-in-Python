# What will be printed in the console when the following code is run?

def bar():
    my_variable = 9
 
    if 16 > 9:
      my_variable = 16
 
    print(my_variable)
 
bar()
#prints: 16
# Remember that in Python there is no block scope. Inside a if/else/for/while code block is the same as outside it.