alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def caeser(cipher_direction, plain_text, shift_amount):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1 #shift amount of 5 times -1 is -5
    for each_letter in plain_text: 
        position = alphabet.index(each_letter)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"The {cipher_direction} message is: {end_text}")
       
            
caeser(direction, text, shift)