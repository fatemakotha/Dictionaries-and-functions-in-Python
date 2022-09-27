# Write a Python program to convert them into a dictionary in a way that item from list1 is the key and item from list2 is the value

keys = ['Ten', 'Twenty', 'Thirty'] #....list1
values = [10, 20, 30] #....list2

#Function to merge two LISTS to form a DICTIONARY:

def make_list(list1, list2):
    dic = {}
    dic[keys[0]] = values[0]
    dic[keys[1]] = values[1]
    dic[keys[2]] = values[2]
    print(dic)

make_list(keys, values) #list1 = keys and list2 = values