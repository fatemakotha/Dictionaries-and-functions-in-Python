#Local Scope

def drink_potion():
    potion_strength = 2 #when you create a new variable inside a function its only accessible only when inside that function, because it has LOCAL SCOPE
    print(potion_strength)
drink_potion() #prints: 2

print(potion_strength) #prints error