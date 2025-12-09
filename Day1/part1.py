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
        curr=(curr+dis)%100
    else:
        curr=(curr-dis+100)%100
    if(curr==0):
        res+=1
print(res)

