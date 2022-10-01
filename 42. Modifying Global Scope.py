#Modifying Global Scope

enemies = 1 #variable has Global Scope

def increase_enemies():
    global enemies
    enemies = 2
    print(f"enemies inside function: {enemies}") #prints: f"enemies inside function: {enemies}"

increase_enemies()
print(f"enemies outside function: {enemies}") #prints: f"enemies inside function: {enemies}"