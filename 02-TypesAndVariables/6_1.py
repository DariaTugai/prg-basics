###
# A program that calculates the number of characters
# of your name, surname and full name
#
name = 'Daria'   # replace Anna with your name
surname = 'T' # replace May with your surname
characters_in_name = len(name)
charsur=len(surname)
print(f'Your name has {characters_in_name} characters')
print(f'Your surname has {charsur} characters')
print(f'Your full name has {characters_in_name+charsur} characters') # with a space between name and surname