###
# Saves to a file a list of employees working at a specified position.
#

# file names
employees_file = 'it_company.csv'
position_file = 'software_engineer.txt'

# Position
job_title = 'Software Engineer'

# write selected employees to a file
with open(employees_file,'r') as f1:
   with open(position_file,'w') as f2:
    #   cont=f1.read()
      for line in f1:
         if job_title in line:
            f2.write(line)
            # f2.write('\n')