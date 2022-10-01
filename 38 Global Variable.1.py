#Global Scope
player_health = 10 #variables set OUTSIDE any FUNCTION are GLOBAL variables

def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)
drink_potion() #prints: ERROR because drink_potion is now inside game() which means it is now a LOCAL variable