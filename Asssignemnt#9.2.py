class Resturant():
    def __init__(self,name,cuisine_type):
        self.name=name
        self.cuisine=cuisine_type
    def descirbe_resturant(self):
        print(self.name,' serves wonderfull',self.cuisine)
    def open(self):
        print(self.name,'   is open come on in')
resturant=Resturant('Bundo','pizza')
resturant.descirbe_resturant()
resturant.open()



