cs=input('Are you interested in computer science? (y/n): ') =='y'
cg=input('Do you like playing computer games? (y/n): ') =='y'
ig=input('Do you have an Instagram account? (y/n): ') =='y'
ics='No'
icg='No'
iig='No'
if cg:
    icg='Yes'
if cs:
    ics='Yes'
if ig:
    iig='Yes'
print(f'SURVEY RESULTS Interested in computer science: {ics} Playing computer games: {icg} Has an Instagram account: {iig}')