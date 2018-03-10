def arr():
    while True:

        age = int(input("What's Your age"))

        if age>=1 and age<=3:
            print('free')
        elif age>3 and age <13:
            print('the ticket is 10$')
        else :
            print('the ticket is 15$')
a=arr()
print(a)