# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements
food=0
transport=0
utilities=0
weeks=[]

for i in monthly_expenses:
    food+=i[0]
    transport+=i[1]
    utilities+=i[2]    
    weeksum=0 
    for j in i:
        weeksum+=j
    weeks.append(weeksum)

# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:',food)
print('Transport:',transport)
print('Utilities:',utilities)
print('Week 1:',weeks[0])
print('Week 2:',weeks[1])
print('Week 3:',weeks[2])
print('Week 4:',weeks[3])
print('---------------')
print('TOTAL:',weeks[0]+weeks[1]+weeks[2]+weeks[3])