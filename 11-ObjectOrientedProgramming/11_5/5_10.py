class C():
    def __init__(self,arr):
        self.coordinates=arr
        self.is_ok=False

    def m(self,n):
        count=0
        for i in self.coordinates:
            if i[0]>0 and i[1]>0:
                count+=1
        if count>=n:
            self.is_ok=True
    
    def ret(self):
        print(self.is_ok)

p1=C([[2,3],[1,8],[-6,4],[3,-7]])
p1.m(3)
p1.ret()
