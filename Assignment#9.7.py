class user():
    def __init__(self,first_name,last_name,username,email):
        self.name=first_name
        self.lname=last_name
        self.user_name=username
        self.email=email


    def describe_user(self, *option):
        print('name',self.name,'\nlast name',self.lname,'\nusername',self.user_name,'\nemail',self.email )


    def greet_user(self):
        print()

class Admin(user):
    def __init__(self,name,lname,user_name,email):
        super().__init__(name,lname,user_name,email)
        self.privilidges=[]
    def show_privilidges(self):
        for privlidges in self.privilidges:
            print(privlidges)
sow=Admin('Ahsan','khan','khanahsan530','khanahsan530@gmai')
sow.describe_user()
sow.privilidges=['hoe','sss','sdff']
sow.show_privilidges()

