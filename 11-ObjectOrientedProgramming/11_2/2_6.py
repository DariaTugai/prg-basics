class Phone():
    def __init__(self, brand,model, price):
        self.brand= brand
        self.model = model
        self.price = price
        self.on= False

    def phone_on(self):
        self.on= True

    def phone_off(self):
        self.on= False

    def prise_up(self, amount):
        self.price+= float(amount)

    def display_info(self):
        print(f'Phone brand is {self.brand}, phone model is {self.model} phone price is {self.price}')
        if self.on:
            print('The phone is currently on.')
        else:
            print('The phone is currently off.')

def main():
    my_phone= Phone('samsung','A54',600)
    my_phone.prise_up(250)
    my_phone.phone_on()
    my_phone.display_info()


main()

        



   
      