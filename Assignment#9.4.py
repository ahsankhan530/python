class Resturant():
    def __init__(self,name,cuisine_type,number_served):
        self.name=name
        self.cuisine=cuisine_type
        self.number_served=number_served
    def descirbe_resturant(self):
        print(self.name,' serves wonderfull',self.cuisine)
    def open(self):
        print(self.name,'   is open come on in')
    def set_numberserved(self,number_served):
        self.number_served=number_served

    def increment_numberserved(self,additional_number):
        self.number_served+=additional_number
resturant=Resturant('Bundo khan','Pizza',4)
resturant.descirbe_resturant()
resturant.number_served=3
print(resturant.number_served)
resturant.set_numberserved(3)
print(resturant.number_served)
resturant.increment_numberserved(3)
print(resturant.number_served)
