def manufacture_car(manufacture,model,**option):
    car={}
    car['model']=model
    car['manufacture']=manufacture
    for k,v in option.items():
        car[k]=v
    return car
#m_car=manufacture_car('Honda','1991',color='blue',two_package=True)
#print(m_car)
def make_sandwitch(*items):
    print("your following item is\n",items)
    for item in items:
        print(item,' is added')
make_sandwitch('chiken','cheese','charde')
make_sandwitch('beef','e','e')

def cal():

    user=input('plz select the operation')
    for i in range(0,3) :
       i=int(input('witdraw'))
       b=i
    return b
    for r in range(0,3):
        r=int(input('deposit'))

cal()
