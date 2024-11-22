# This code is for educational purposes only

import string

def shift(char, encoder):
    # due to mod of 26, shifting with respect to assci is needed otherwise the cipher txt will not map in lower case range
    if char.islower():
       return chr((ord(char) - ord('a')+encoder) % 26 + ord('a'))  
    elif char.isupper():
       return chr((ord(char) - ord('A')+encoder) % 26 + ord('A'))
     

def encode(txt):
    encoder = int(input("Enter key: (0-255): "))   # for simplicity the key is mapped with assci but the size of key is variable
    code = []
    for char in txt:
      if char in string.ascii_letters:   # 1st check if input is alphabetic in nature then process lower or/and upper case characters of the input
       encoded = shift(char, encoder)
      else:
#       encoded = char # case when non-alphabetic remain same
       encoded = chr((ord(char) + encoder) % 256)  # simply shift assci value by encoder size    
      code.append(encoded) # 
    return ''.join(code)
          
txt = input("Enter text:\n")
print ("Plaintext: ",txt)
code = encode(txt)
print ('Encoding...')
print("Cipher: ",code)