#There is NO Block Scope
game_level = 3

def create_enemy():
    enemies = ["Skeletons", "Zombies", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]
    print(new_enemy)
#print(new_enemy) #prints: ERROR due to no indentation

create_enemy() #prints: Skeletons