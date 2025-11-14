###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''


for char in plain_text:
    if char.isalpha():
        encrypted_text=encrypted_text+ f'{chr(int(ord(char))+3)}'
    else:
        encrypted_text=encrypted_text+ char
   
print(plain_text)
print(encrypted_text)