

class Resturant():

    def __init__(self,name,cuisine_type):
        self.name=name
        self.cuisine=cuisine_type
    def descirbe_resturant(self):
        print(self.name,' serves wonderfull',self.cuisine)
    def open(self):
        print(self.name,'   is open come on in')

class IceCreamStand (Resturant):
    def __init__(self,name,cuisine_type='ice cream'):
        super().__init__(name,cuisine_type)
        self.flavor=[]
    def showflavor(self):
        print('we have the following flavor')
        for flavor in self.flavor:
            print('-',flavor)
    def book_order(self):
        print('Plz book Your order')


        for book in self.flavor:
         book = input()
         if book==('strawberry'or'Strawberry'):
             print('quantity')
             quantity=input()

             print(quantity,' strawberry')
             print('ok...something else')
         elif book==('vanila'or 'Vanila'):
            print('plz tell me quantity')
            quantity2=input()
            print(quantity2,'vanila')
            print(' something else')

         elif book==('Pista'or 'pista'):
            print('plz tell me quantity')
            quantity3=input()
            print(quantity3,'Pista')
            print('something else')
         else:

            print('finished')
            break


big_one=IceCreamStand('Bundo')
big_one.descirbe_resturant()
big_one.flavor=['Strawberry','pista','vanila']
big_one.showflavor()
big_one.book_order()
