###
# Checks the correctness of username and password
#
import re

# read username and password from keyboard
username = input('Enter username: ')
password = input('Enter password: ')

# pattern (criteria) for username and password
username_pattern = '^[a-z]{6,}$'
password_pattern = '^(?=.*[A-Z])(?=.*[a-z]).{8,}$'


# check if username and password are ok
username_match = re.match(username_pattern,username)
pass_match= re.match(password_pattern,password)

# print results
if username_match and pass_match:
   print('yep')
else:
   print('n')
#    username is at least 6 characters long
# username contains only lowercase letters
# password is at least 8 characters long
# password contains only letters (lowercase and uppercase), numbers, and the underscore character