
g={}
with open("input.txt","r") as f:
    for i in f:
        s=i.strip()
        u,ot=s.split(": ")
        g[u]=ot.strip().split()

col=set()
cnt={}
def dfs(u):
    if(u=="out"):
        return 1
    if u in col:
        return cnt.get(u,0)
    col.add(u)
    res=0
    for v in g.get(u,[]):
        res+=dfs(v)
    cnt[u]=res
    return res
print(dfs("you"))