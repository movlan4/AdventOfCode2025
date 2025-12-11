data=[]
with open("input.txt","r") as f:
    for l in f:
        now=[]
        for i in l.strip():
            if i=='.':
                now.append(0)
            else:
                now.append(1)
        data.append(now)
n=len(data)
m=len(data[0])
tot=0
while True:
    res=0
    for i in range(n):
        for j in range(m):
            cnt=0
            if data[i][j]==1:
                if i!=0:
                    if j!=0:
                        cnt+=data[i-1][j-1]
                    if j!=m-1:
                        cnt+=data[i-1][j+1]
                    cnt+=data[i-1][j]
                if j!=0:
                    cnt+=data[i][j-1]
                if j!=m-1:
                    cnt+=data[i][j+1]
                if i!=n-1:
                    if j!=0:
                        cnt+=data[i+1][j-1]
                    if j!=m-1:
                        cnt+=data[i+1][j+1]
                    cnt+=data[i+1][j]
                if cnt<4:
                    res+=1
    if res==0:
        break
    for i in range(n):
        for j in range(m):
            cnt=0
            if data[i][j]==1:
                if i!=0:
                    if j!=0:
                        cnt+=data[i-1][j-1]
                    if j!=m-1:
                        cnt+=data[i-1][j+1]
                    cnt+=data[i-1][j]
                if j!=0:
                    cnt+=data[i][j-1]
                if j!=m-1:
                    cnt+=data[i][j+1]
                if i!=n-1:
                    if j!=0:
                        cnt+=data[i+1][j-1]
                    if j!=m-1:
                        cnt+=data[i+1][j+1]
                    cnt+=data[i+1][j]
                if cnt<4:
                    data[i][j]=0
                    tot+=1

print(tot)

