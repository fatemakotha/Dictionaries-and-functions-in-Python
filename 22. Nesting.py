#Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stutthart"],
}

# Nesting a Dictionary in a Dictionary

travel_diary = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"]},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stutthart"]},
}

print(travel_diary)
#prints:
# {'France': {'cities_visited': ['Paris', 'Lille', 'Dijon']}, 'Germany': {'cities_visited': ['Berlin', 'Hamburg', 'Stutthart']}}