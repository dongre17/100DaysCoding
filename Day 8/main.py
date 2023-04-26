# import
import art
import math

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(text, shift):
    
    cipher_text = ''

    for char in text:        
        try:
          value_index = alphabet.index(char)
        except:
          value_index = -1

        if value_index > -1:           
            if (value_index + shift) > (len(alphabet) - 1):              
              value_index = (value_index + shift) % 26
            else:
              value_index = value_index + shift 
           
            cipher_text += alphabet[value_index]
            
        else:
           cipher_text += char

    print(cipher_text)

def decrypt(text, shift):
    
    cipher_text = ''

    for char in text:        
        try:
          value_index = alphabet.index(char)
        except:
          value_index = -1

        if value_index > -1:           
            if (value_index - shift) < 0:              
              value_index = len(alphabet) - abs(value_index - shift)
            else:
              value_index = value_index - shift 
           
            cipher_text += alphabet[value_index]
            
        else:
           cipher_text += char

    print(cipher_text)






    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

if direction == 'encode':
   encrypt(text, shift=shift)
else:
   decrypt(text, shift=shift)