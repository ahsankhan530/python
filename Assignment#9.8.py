class privlidges():
    def __init__(self):
        self.privlidges=[]

    def show_privilidges(self):
        for privlidges in self.privilidges:
            print(privlidges)

class Admin(privlidges):
    def __init__(self):
        self.pvg=privlidges()


sow=Admin()
sow.privilidges=['can add post','can ban post','sdff']

sow.pvg.privlidges=['can ban','can add','can remove']
sow.show_privilidges()


