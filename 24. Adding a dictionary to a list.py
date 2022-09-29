#Adding a dictionary to a list
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]


#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country, visits, cities):
    new_country =  {}
    new_country["country"] = "Russia"
    new_country["visits"] = "2"
    new_country["cities"] = ["Moscow", "Saint Petersburg"]
    travel_log.append(new_country)
    
    

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
#prints
# [{'country': 'France', 'visits': 12, 'cities': ['Paris', 'Lille', 'Dijon']}, {'country': 'Germany', 'visits': 5, 'cities': ['Berlin', 'Hamburg', 'Stuttgart']}, {'country': 'Russia', 'visits': '2', 'cities': ['Moscow', 'Saint Petersburg']}]