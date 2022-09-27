alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, shift_amount):
    """Shifts each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text. """
    cipher_text = "" #set to an empty string
    for each_letter in plain_text: #plain_text = hello, each_ letter = "h" then "e" then "l" then "l" then "o" 
        position = alphabet.index(each_letter) #finds the position of "h" then "e" then "l" then "l" then "o". For eg: Position for "h" is the 7th index. Thus position = 7
        new_position = position + shift_amount #if shift_amount is 5, new_position = 7 + 5 which is 12
        cipher_text += alphabet[new_position] # fpr each_letter it replaces the position and keeps adding to the string named ciper_text
    print(f"The encoded text is {cipher_text}")

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(plain_text, shift_amount):
    """Shifts each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text."""
    decipher_text = "" #set to an empty string
    for each_letter in plain_text: #plain_text = hello, each_ letter = "h" then "e" then "l" then "l" then "o" 
        position = alphabet.index(each_letter) #finds the position of "h" then "e" then "l" then "l" then "o". For eg: Position for "h" is the 7th index. Thus position = 7
        new_position = position - shift_amount #if shift_amount is 5, new_position = 7 - 5 5 which is 2
        decipher_text += alphabet[new_position] # fpr each_letter it replaces the position and keeps adding to the string named ciper_text
    print(f"The decoded text is {decipher_text}")
 

#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

if direction == "encode":
    encrypt(text, shift) 
else:
    decrypt(text, shift) 