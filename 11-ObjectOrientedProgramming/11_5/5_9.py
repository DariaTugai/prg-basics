class C():
    def __init__(self,name,surname,age,seniority):
        self.name=name
        self.surname=surname
        self.age=age
        self.seniority=seniority
    
    def define(self):
        if self.age>=18:
            print(f'{self.surname.upper()}{self.name[0].upper()}{self.seniority}')
        else:
            print(f'{self.surname.lower()}{self.name[0].lower()}{self.seniority}')

    
p1=C('Anna','May',17,7)
p1.define()

p2=C("George","Brown",21,4) 
p2.define()
