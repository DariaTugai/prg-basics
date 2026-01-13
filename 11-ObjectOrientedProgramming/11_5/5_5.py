import random
class Thermometer():
    def __init__(self):
        self.temperature= random.randint(340,420)/10
        self.fever=False
    

    def ret_data(self):
        if self.temperature>=37.0 and self.temperature<=41.0:
            print(f'Temperature: {self.temperature} (fever)')
        elif self.temperature>=41.0:
            print(f'Temperature: {self.temperature} (CRITICAL TEMPERATURE!!)')
        else:            
            print(f'Temperature: {self.temperature}')

one=Thermometer()
one.ret_data()




