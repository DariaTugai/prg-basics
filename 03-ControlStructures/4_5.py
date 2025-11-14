###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    encrypted_text= encrypted_text + f'{ord(char)}'
for char in encrypted_text:
    if char.isdigit():
        encrypted_text= encrypted_text+ f'{(int(char)) + 3}'
    else:
        encrypted_text= encrypted_text+ char
for char in encrypted_text:
    if char.isdigit():
         encrypted_text= encrypted_text+ f'{chr(int(char))}'
    else: 
        encrypted_text= encrypted_text + char

print(plain_text)
print(encrypted_text)