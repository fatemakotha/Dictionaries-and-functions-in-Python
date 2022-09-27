# Define a function called paint_calc() so that the code below works. 
def paint_calc(height, width, cover):
    number_of_cans = round((test_h * test_w) / coverage)
    print(f"No of cans needed: {number_of_cans}")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
#prints:
# Height of wall: 50
# Width of wall: 20
# No of cans needed: 200