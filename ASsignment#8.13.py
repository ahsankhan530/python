def build_profile(first_name,last_name,**user_info):
    person={}
    person['first_name']=first_name
    person['last_name']=last_name
    for key,value in user_info.items():
        person[key]=value
    return person
user_profile=build_profile('Ahsan','khan',location='karachi',subject='cs')
user_profil=build_profile('jawad','Ahmed',location='kemari',sub='bba')
print(user_profile)
print(user_profil)
