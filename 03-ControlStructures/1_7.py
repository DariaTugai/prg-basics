basic_salary = 5000
total_salary = 0
bonus = 0.15 # 15%
is_bonus = input('Does the employee receive a bonus? (Y/N):') == 'Y'

if is_bonus == True:
    total_salary = basic_salary + bonus*basic_salary 
    print("Total salary",total_salary)
else:
    total_salary = basic_salary
    print("Total salary", total_salary)
    print('No bonus applied')