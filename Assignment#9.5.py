class user():
    def __init__(self):
        self.name=''
        self.lname=''
        self.user_name=''
        self.email=''
        self.login_attempt=''
    def getinput(self):
        self.name=input()
        self.lname=input()
        self.user_name=input()
        self.email=input()


    def describe_user(self, *option):
        print(
            'name',self.name,'\nlast name',self.lname,'\nusername',self.user_name,'\nemail',self.email )


    def greet_user(self):
        print()
User=user()
User.getinput()
#User=user('Ahsan','khan','khanahsan530','khnaahsan530@gmail.com')
User.describe_user()
print('\n')
# User2=user('Abbas','ali','abbasali310','abbas350@gmail.com')
# User2.describe_user()
