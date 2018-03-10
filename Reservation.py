import random
class Reservation():
    def condition(self,user_input):
        a=self.user_input=int(input('Press 1 for Businnes\n2) press 2 for Economy'))
        if a==1:
            b=Businnes()
            b.Adult(0,0)
            b.child(0,0)
            b.total_ticket()
            b.total()
            with open('ab.txt','w') as f:
                f.write(str(b.total()))
        elif a==2:
            e=Economoy()
            e.Adult(0,0)
            e.child(0,0)
            e.total_ticket()
            e.total()
        elif a==3:
            list=['pakistan Express','Busin','shalimar','night']
            print(random.choice(list))

class Businnes():
    def child(self,result,num_child,child_price=800,ran=0):
        self.num_child=int(input('Number of child '))
        self.result=child_price*self.num_child

    def Adult(self,re,num_ad,adut_price=2000):

        self.num_ad=int(input('Number of adult'))
        self.re=adut_price*self.num_ad

    def total(self):
        print('Total price is ',self.result+self.re)
    def total_ticket(self):
        for i in range(self.num_child+self.num_ad):
            g = self.ran = random.randint(200, 300)
        print('seats number',g, 'to', g + self.num_child+self.num_ad)
        print('Total seats ',self.num_child+self.num_ad,'\n',self.num_ad,'adult seats','\n',self.num_child,' child seats')
class Economoy():
    def child(self):
        a = self.child_price = 500
        num_child = input()
        result = a * num_child
        print('Price of child is', result)

    def Adult(self, re, num_ad, adut_price=1500):
        self.num_ad = int(input('Number of adult'))
        self.re = adut_price * self.num_ad
        print('price of adult price is ', self.re)

    def total(self):
        print('Total price is ', self.result + self.re)

    def total_ticket(self):
        for i in range(self.num_child+self.num_ad):
            g = self.ran = random.randint(200, 300)
        print('seats number',g, 'to', g + self.num_child+self.num_ad)
        print('Total seats ', self.num_child + self.num_ad, '\n', self.num_ad, 'adult seats', '\n', self.num_child,
              ' child seats')
Re=Reservation()
Re.condition(0)
