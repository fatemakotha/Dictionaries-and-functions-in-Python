def outer_function(a, b): #a = 5, b - 10
    def inner_function(c, d): #this means c = 5 and d = 10
        return c + d #c + d = 5 + 10 = 15
    return inner_function(a, b) #returns 15
 
result = outer_function(5, 10) #15
print(result)
#prints:
#15