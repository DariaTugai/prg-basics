class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km

    def print_receipt(self):
        print(f'Tou travelled {self.distance} km, rate per km is {self.rate_per_km}, the fair is {self.fare}.')


one=TaxiRide(3) 
one.calculate_fare(4)
one.print_receipt()
