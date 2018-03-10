tomy={'Dog':'Rasheed'}
shono={'cat':'ali'}
bholo={'Goat ':'Nabeel'}
animals=[tomy,shono,bholo]

for animal in animals:
    for key,value in animal.items():
        print('pet type',key,'owner name',value)