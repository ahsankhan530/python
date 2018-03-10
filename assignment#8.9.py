
def show_magician(magicians):

    for magician in magicians:
        print(magician)


def makegreat(magicians):
    great_magicians=[]
    while magicians:
        magician=magicians.pop()
        great_magician=magician+'the great '
        great_magicians.append(great_magician)
        for great_magician in great_magicians:
            magicians.append(great_magician)

magicians = ['rock', 'jhon', 'michel', 'bravo']
show_magician(magicians)
makegreat(magicians)
show_magician(magicians)