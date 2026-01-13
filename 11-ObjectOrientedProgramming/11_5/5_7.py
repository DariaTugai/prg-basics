class Statistics():
    def __init__(self):
        self.numbers=[]
        self.maximum=''
        self.minimum=''
        self.meann=''
        self.median=''

    def add(self,number):
        self.numbers.append(number)

    def display_all(self):
        for i in self.numbers:
            print(i,end=' ')

    def maxim(self):
        self.maximum= (max(self.numbers))

    def minim(self):
        self.minimum=(min(self.numbers))

    def arithmetic_mean(self):
        sum=0
        count=0
        for i in self.numbers:
            sum+=i
            count+=1
        self.meann=sum/count
    
    def media(self):
        if len(self.numbers)%2==0:
            self.median=((self.numbers[len(self.numbers)//2]+self.numbers[(len(self.numbers)//2)-1]))//2
        else:
            self.median= (self.numbers[len(self.numbers)//2])
            
    def ret_data(self):
        print(f'Min is {self.minimum}, max is {self.maximum}, median is {self.median}, mean is {self.meann}')

ar=Statistics()
ar.add(12)
ar.add(37)
ar.add(6)
ar.add(9)
ar.add(17)
ar.add(17)
ar.media()
ar.maxim()
ar.minim()
ar.arithmetic_mean()
ar.ret_data()