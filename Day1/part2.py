data=[]
with open("input.txt","r") as f:
    for l in f:
        data.append(l.strip())
curr=50
res=0
for i in data:
    dir=i[0]
    dis=int(i[1:])
    if(dir=='R'):
        if(curr+dis>=100):
            res+=(curr+dis)//100
        curr=(curr+dis)%100
    else:
        if curr == 0:
            res += dis // 100
        elif dis >= curr:
            res += (dis - curr) // 100 + 1
        curr=(curr-dis)%100
print(res)

