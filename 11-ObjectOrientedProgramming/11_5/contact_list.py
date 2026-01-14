class Contact_List:
    def __init__(self,mlist=[]):
        self.list=mlist

    def add(self,contact):
        self.list.append(contact)

    def display(self):
        for object in self.list:
            print(object.name,object.email,object.phone)  