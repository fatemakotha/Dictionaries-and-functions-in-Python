#Function that take a dictionary and splits it to make a list
def test(dictt):
    result = list(map(list, dictt.items()))
    return result    

color_dict = {1 : 'red', 2 : 'green', 3 : 'black', 4 : 'white', 5 : 'black'}
print(color_dict) #{1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}

#Convert the said dictionary into a list of lists:
result1 = test(color_dict)
print(result1) #[[1, 'red'], [2, 'green'], [3, 'black'], [4, 'white'], [5, 'black']]

color_dict = {'1' : 'Austin Little', '2' : 'Natasha Howard', '3' : 'Alfred Mullins', '4' : 'Jamie Rowe'}
print(color_dict) #{'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}

#Convert the said dictionary into a list of lists:
result2 = test(color_dict)
print(result2) #[['1', 'Austin Little'], ['2', 'Natasha Howard'], ['3', 'Alfred Mullins'], ['4', 'Jamie Rowe']]