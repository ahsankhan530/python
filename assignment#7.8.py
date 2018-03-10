sandwitch_order=['tuna sandwitch','cheeze sandwitch','chicken sandwitch']
finished_sandwitch=[]
while sandwitch_order:
    pp=sandwitch_order.pop()
    print('your order',pp)
    finished_sandwitch.append(pp)
    for finished_sandwitc in finished_sandwitch:
        print(finished_sandwitc)
print(sandwitch_order)
