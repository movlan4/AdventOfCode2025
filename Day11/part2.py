from functools import lru_cache




g={}
with open("input.txt","r") as f:
    for i in f:
        s=i.strip()
        u,ot=s.split(": ")
        g[u]=ot.strip().split()

memo={}
def dfs(u,mask):
    if (u,mask) in memo:
        return memo[(u,mask)]
    if(u=="dac"):
        mask|=1
    if(u=="fft"):
        mask|=2
    if(u=="out"):
        if mask==3:
            return 1
    res=0
    for v in g.get(u,()):
        res+=dfs(v,mask)
    memo[(u,mask)]=res
    return res
print(dfs("svr",0))