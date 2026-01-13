class C():
    def __init__(self,data):
        self.data=data

    def m1(self,s,n):
        self.data[s]=n

    def m2(self,s):
        self.sum=0
        for i in s:
            if i in self.data:
                self.sum+=self.data[i]

    def ret(self):
        print(self.data)
        print(self.sum)

p1=C({"A":120,"D":150,"G":90,"K":110})
p1.m1("G",130)
p1.m2("KEJ")
p1.ret()

        