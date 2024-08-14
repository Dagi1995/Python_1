alphabet =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'
          , 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
          'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'
          , 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]

direction = input("type 'encode' to encrypt type 'decode' to decrypt : \n ")

def encrypt(plain_text , shift_amount):
    cipher_text = ""
    for letter in plain_text:
        if letter in alphabet:
           position = alphabet.index(letter)
           new_position = position + shift_amount
           new_letter = alphabet[new_position]
           cipher_text += new_letter
        else:
            cipher_text += letter
   
    print(f"The encrypted word is { cipher_text}")


def decrypt(plain_text , shift_amount):
    cipher_text = ""
    for letter in plain_text:
        if letter in alphabet:
          position = alphabet.index(letter)
          new_position = position - shift_amount
          new_letter = alphabet[new_position]
          cipher_text += new_letter
        else:
            cipher_text += letter

    print(f"The encrypted word is { cipher_text}")


if direction == 'encode':
   text = input("Type your massage here :\n").lower()
   shift = int(input("Type the shift number : \n"))
   encrypt( plain_text = text , shift_amount = shift )  

elif direction == 'decode':
   text = input("Type your massage here :\n").lower()
   shift = int(input("Type the shift number : \n"))
   decrypt( plain_text = text , shift_amount = shift )  

else:
    print("YOu write the wrong word")
