def manufacture_car(manufacture,model,**option):
    car={}
    car['model']=model
    car['manufacture']=manufacture
    for k,v in option.items():
        car[k]=v
    return car
m_car=manufacture_car('Honda','1991',color='blue',two_package=True)
print(m_car)