# import requests
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# from matplotlib import style
# style.use('fivethirtyeight')
# fig=plt.figure()
# ax1=fig.add_subplot(1,1,1)
# def animate(i):
#     graph_data=open('ab.txt','r').read()
#     lines=graph_data.split('\n')
#     xs=[]
#     ys=[]
#     for line in lines:
#         if len(line)>1:
#             x , y=line.split(',')
#             xs.append(x)
#             ys.append(y)
#     ax1.clear()
#     ax1.plot(xs,ys)
# ani=animation.FuncAnimation(fig,animate,interval=1000)
# # plt.show()
# import numpy as np
# import matplotlib.pyplot as plt
#
# ax = plt.subplot(111)
#
# t = np.arange(0.0, 6.0,0.09)
# s = np.cos(t)
# line, = plt.plot(t, s, lw=-8)
#
#
#
# plt.ylim(-2,2)
# plt.show()

import matplotlib.pyplot as plt
import requests
class crypto():

    def __init__(self,coin,conver_to,data):
        self.coin=coin
        self.convert_to=conver_to

        self.data=data
        self.price=[]
        self.time=[]
    def getCoinList(self):
        url= "https://min-api.cryptocompare.com/data/histohour?fsym="+self.coin.upper()+"&tsym="+self.convert_to.upper()+"&limit="+self.data+"&aggregate=3&e=CCCAGG"
        req=requests.get(url)

        self.fulldata=req.json()['Data']
        for data in self.fulldata:
            self.time.append(float(data['time']))
            self.price.append((float(data['close'])))
    def graph(self):
        plt.plot(self.time,self.price)
        plt.get_scale_names()
        plt.title(self.coin+'price')
        plt.xlabel('time in second')
        plt.ylabel('price in '+self.convert_to.upper())
        plt.show()
# a=crypto('Btc','usd','50')
# a.getCoinList()
# a.graph()
eth=crypto('Eth','USD','30')
eth.getCoinList()
eth.graph()