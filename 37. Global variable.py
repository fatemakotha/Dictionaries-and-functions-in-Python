#Global Scope
player_health = 10 #variables set OUTSIDE any FUNCTION are GLOBAL variables

def drink_potion():
    potion_strength = 2
    print(player_health)
drink_potion() #prints: 10