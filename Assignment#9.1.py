class dog():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sit(self):
        print(self.name,' is now sitting')
    def rollover(self):
        print(self.name+' rolled over')
Dog=dog('wiliam',17)
print(Dog.name)
print(Dog.age)
Dog.sit()
Dog.rollover()
shepherd=dog('tony','17')
shepherd.sit()
                                                                          
