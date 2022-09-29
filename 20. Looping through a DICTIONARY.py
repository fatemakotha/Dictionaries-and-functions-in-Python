#Looping through a DICTIONARY
programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

print(programming_dictionary)

for thing in programming_dictionary: 
    print(thing) #just prints the key
    #prints:
    # Bug
    # Function

for thing in programming_dictionary: 
    print(programming_dictionary[thing]) #just prints the value
    #prints:
    # An error in a program that prevents the program from running as expected.
    # A piece of code that you can easily call over and over again.