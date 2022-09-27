#Function to check for prime numbers:
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("Prime")
    else:
        print("Not prime")

n = int(input("Check this number: ")) # 1. Takes the input from user
prime_checker(number=n) # 2. number = n, number = 2 thus prime_checker(2)

# prints:
# Check this number: 11
# Prime