#-----------------------------------Excercise #6.1----------------------------------
# a=str(input())
# dic={'First name':'Ahsan','Last name':'khan','city':'Karachi'}
#
# print("city name is ",dic['city'])
#==============================================Excercise #6.2========================
favorite_names={'Ahsan':'3','ali':'4','furqan':'7','umair':'9','faisal':'8'}
name=str(input("pls input name "))

coun=0

if name in favorite_names.keys():
    a = str(input('guess the num'))
    if a in favorite_names['Ahsan']:
        print(True,"Excellent")
    else:
        print('sorry right answer is',favorite_names['Ahsan'])
name = str(input("pls input name "))
if name in favorite_names.keys():
    a = str(input('guess the num'))
    if a in favorite_names['ali']:
        print(True)
    else:
        print('Data does not exist')
elif name== 'Exit' or 'exit':
    SystemExit(0)
else:
    print('try again')

    #=====================================================
# favorite_names = {'Ahsan': '3', 'ali': '4', 'furqan': '7', 'umair': '9', 'faisal': '8'}
# name = str(input("pls input name "))
#
# for name in favorite_names:
#     if name in favorite_names.keys():
#         print(name)
#         a = str(input('guess the num'))
#         if a in favorite_names.values():
#             print(a)
#         else:
#             print('')
#
#     else:
#         print('try again')
# print('write answer is ',favorite_names)
#========================================================================

# favorite_names={'Ahsan':'3','ali':'4','furqan':'7','umair':'9','faisal':'8'}
# for key ,value in favorite_names.items():
#     print (key,'Your favorite number is ',value)