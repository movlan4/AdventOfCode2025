data=[]
with open("input.txt","r") as f:
    for l in f:
        data.append(l.strip())
res=0
for i in data:
    mx1=-100
    best=-1
    for j in range(0,len(i)):
        if best<mx1*10+int(i[j]):
            best=mx1*10+int(i[j])
        mx1=max(int(i[j]),mx1)
    res+=best
print(res)
