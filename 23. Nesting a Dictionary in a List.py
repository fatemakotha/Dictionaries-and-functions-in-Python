#Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stutthart"],
}

# Nesting a Dictionary in a List

travel_log = [
    {
        "country": "France", 
        "cities": ["Paris", "Lille", "Dijon"],
        "total_visits": 24
    },
    {
        "country": "Germany",
        "cities": ["Berlin", "Hamburg", "Stutthart"],
        "total_visits": 454},
]

print(travel_log)
#prints:
# [{'country': 'France', 'cities': ['Paris', 'Lille', 'Dijon'], 'total_visits': 24}, {'country': 'Germany', 'cities': ['Berlin', 'Hamburg', 'Stutthart'], 'total_visits': 454}]