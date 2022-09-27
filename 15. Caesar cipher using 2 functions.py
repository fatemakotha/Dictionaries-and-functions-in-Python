alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet: #iIf the user enters letter only then the code below runs, if user enters a symbol or a number, it stays the same 
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    else:
        end_text += char #for symbols i.e. char = %, then that char is added to the end text
    
  print(f"Here's the {cipher_direction}d result: {end_text}")
  



#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26 #takes the shift amount and dvides it by 25(no of alphabets) as many times needed, to make the remainder 0
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    question = input("Do you want to go again? ")
    if question == "no":
        should_continue = False
        print("GOODBYE")
