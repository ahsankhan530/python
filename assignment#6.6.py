names={'Ahsan':'python','Furqan':'java','nabeel':'c#','Ali':'c'}
list=['Ahsan','JAwad','nabeel','Ali']
for name in names:
    if name in names.keys():
        print('Thanks',name,'\n','You voted for',names[name])
