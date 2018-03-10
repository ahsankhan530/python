from random import randint
class Die():
    def input(self):
        print()
    def roll_dice(self):
        for player in range(1,4):
            print('player ',player)
            for a in range(5):
                a = randint(1, 6)
                if a==6  :
                    print(a,'again')
                else:
                    print(a)
                    break

a=Die()
a.roll_dice()
