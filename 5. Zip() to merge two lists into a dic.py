# Write a Python program to convert them into a dictionary in a way that item from list1 is the key and item from list2 is the value

keys = ['Ten', 'Twenty', 'Thirty'] #....list1
values = [10, 20, 30] #....list2

#Function to merge two LISTS to form a DICTIONARY:
def merge(list1, list2):
    dictionary = dict(zip(keys, values))
    print(dictionary)

merge(keys, values) 
#prints: {'Ten': 10, 'Twenty': 20, 'Thirty': 30}