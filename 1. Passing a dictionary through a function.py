dictionary = {
    "name": "Kotha",
    "work": "Student",
    "age": "medium",
    "height": "above average",
}
news = {
    "1": ".......",
    "2": "hihihi",
    "3": "+++++++",
    "4": "/ / / / ",
}

print(dictionary) #{'name': 'Kotha', 'work': 'Student', 'age': 'medium', 'height': 'above average'}
print("\n")
print(news) #{'1': '.......', '2': 'hihihi', '3': '+++++++', '4': '/ / / / '}
print("\n")
print("\n")
print("\n")



#function that adds  the VALUE Bangladesh for the KEY "country" to each dictionary when they are passed through a function:
def add(dic):
    dic["counrty"] = "Bangladesh"
    print(dic)

    
add(dictionary) #{'name': 'Kotha', 'work': 'Student', 'age': 'medium', 'height': 'above average', 'counrty': 'Bangladesh'}
print("\n")

add(news) #{'1': '.......', '2': 'hihihi', '3': '+++++++', '4': '/ / / / ', 'counrty': 'Bangladesh'}