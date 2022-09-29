from replit import clear
logo = "--___--"
print(logo)


dic = {}
should_continue = True

def highest_bidder(dic): #passing in, the dic {'kotha': 88, 'cutu': 100}
    highest_score = 0 #highest_score set to 0 to be able to compare
    for bidder in dic: #for "Kotha" in dic, then for "cutu" in dic
        score = dic[bidder] #score set to dic["Kotha"] for which value is 88
        if score > highest_score:
            highest_score = score
    print(f"Highest bidder is {bidder} with a score: {highest_score}")
    



while should_continue:
    name = input("Enter your name: ")
    amount = int(input("Enter your bid amount: "))
    dic[name] = amount
    
    question = input("Are there more bidders? ")
    
    if question == "no":
        should_continue = False
        print(dic) #prints: {'kotha': 88, 'cutu': 100}
        highest_bidder(dic)
    else:
        clear()