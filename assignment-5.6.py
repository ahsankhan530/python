person=int(input())
if person<2:
    print("baby")
elif person==2 or person<4:
    print("toddler")
elif person==4 or person<=13:
    print("person is  a kid")
elif person==13 or person<=20:
    print("tenager")
elif person==20 or person<65:
    print("adult")
elif person>=65:
    print("elder")