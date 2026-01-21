from collections import deque


a = input().split()


q = deque()


dic = dict()



q.append((0,list(map(str,[1,2,3,4,5,6,7,8])),-1))
while q:
    cnt,now,last = q.popleft()
    
    snow = "".join(now)
    if snow in dic:
        continue
    else:
        dic[snow] = 1
    
    for i in range(8):
        if now[i]!=a[i]:
            break
    else:
        print(cnt)
        break
    if last!=0:
        q.append((cnt+1,now[::-1],0))
    temp1 = [now[3]]+now[:3]
    temp2 = now[5:8]+[now[4]]
    
    q.append((cnt+1,temp1+temp2,1))
    
    temp = now[::1]
    temp[1],temp[2],temp[5],temp[6] = temp[2],temp[5],temp[6],temp[1]
   
    q.append((cnt+1,temp,2))
    if last!=3:
        now[0],now[4] = now[4],now[0]
        #print(now)
        q.append((cnt+1,now,3))

    
    
