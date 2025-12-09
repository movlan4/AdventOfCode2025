data=[]
with open("input.txt","r") as f:
    for l in f:
        data.append(l.strip())

res=0
for i in data:
    best=0
    if len(i)<=12:
        best=int(i)
    else:
        st=[]
        rem=len(i)-12
        for ch in i:
            while st and rem>0 and st[-1]<ch:
                st.pop()
                rem-=1
            st.append(ch)
        best=int("".join(st[:12]))
    res+=best
print(res)

