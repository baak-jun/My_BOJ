import sys
def input():return sys.stdin.readline().rstrip()


cnt = 0
a = input()

b = len(a)
last = ")"
mh = 0
for i in range(b):
    
    if a[i]=="(":
        cnt+=1
        last = "("
    else:
        mh = max(mh,cnt)
        last = ")"
        cnt-=1


zido = [["." for i in range(b)] for i in range(mh)]

    


now = (mh-1,0)

for i in range(b):

    if a[i]=="(":
        zido[now[0]][now[1]] = "/"
        if a[i+1]==")":
            now = (now[0],now[1]+1)
        else:
            now = (now[0]-1,now[1]+1)
        
    else:
        zido[now[0]][now[1]] = "\\"
        if i+1<b and a[i+1]=="(":
            now = (now[0],now[1]+1)
        else:
            now = (now[0]+1,now[1]+1)

for i in range(mh):
    print(*zido[i],sep = "")

    
    
