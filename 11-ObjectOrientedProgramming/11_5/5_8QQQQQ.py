class Contact():
    def __init__(self,name,mail,phone):
        self.name=name
        self.email=mail
        self.phone=phone

class Contact_List:
    def __init__(self):
        self.list=[]

    def add(self,contact):
        self.list.append(contact)

    def display(self):
        for i in self.list:
            print(i)    

user1=Contact()
user1.name = 'John Brown'
user1