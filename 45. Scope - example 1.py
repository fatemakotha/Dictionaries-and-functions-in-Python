# What will be printed in the console when the following code is run?


def a_function(a_parameter):
    a_variable = 15
    return a_parameter
 
a_function(10)
print(a_variable)
#prints: NAME ERROR
#It's trying to print a variable that is local to a_function() and is only available inside the function.