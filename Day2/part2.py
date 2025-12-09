f=open("input.txt","r")
data=f.read().split(",")
f.close()
def check(x):
    s=str(x)
    curr=""
    for i in s:
        curr+=i
        if len(s)%len(curr)==0 and len(s)//len(curr)>=2 and (curr*(len(s)//len(curr)))==s:
            return True
    return False
res=0
for i in data:
    l,r=map(int,i.split("-"))
    for j in range(l,r+1):
        if(check(j)):
            res+=j
print(res)