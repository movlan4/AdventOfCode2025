f=open("input.txt","r")
data=f.read().split(",")
f.close()
def check(x):
    s=str(x)
    if(len(s)%2):
        return False
    return s[:len(s)//2]==s[len(s)//2:]
res=0
for i in data:
    l,r=map(int,i.split("-"))
    for j in range(l,r+1):
        if(check(j)):
            res+=j
print(res)