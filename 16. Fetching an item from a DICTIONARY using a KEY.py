#Fetching an item from a DICTIONARY using a KEY
programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

            
print(programming_dictionary)

bugs = programming_dictionary["Bug"] #prints: An error in a program that prevents the program from running as expected.
print(bugs)

new_dictionary = { 123 : "An error in a program that prevents the program from running as expected.", 456: "A piece of code that you can easily call over and over again."}

variable = new_dictionary[456]
print(variable) #prints: A piece of code that you can easily call over and over again.