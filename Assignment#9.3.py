class user():
    def __init__(self,first_name,last_name,username,email):
        self.name=first_name
        self.lname=last_name
        self.user_name=username
        self.email=email


    def describe_user(self, *option):
        print(
            'name',self.name,'\nlast name',self.lname,'\nusername',self.user_name,'\nemail',self.email )


    def greet_user(self):
        print()
User=user('Ahsan','khan','khanahsan530','khnaahsan530@gmail.com')
User.describe_user()
print('\n')
User2=user('Abbas','ali','abbasali310','abbas350@gmail.com')
User2.describe_user()