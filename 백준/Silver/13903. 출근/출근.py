import sys
#import heapq
from collections import deque

def input():return sys.stdin.readline().rstrip()

#q = []
q = deque()

x,y = map(int,input().split())

zido = [list(map(int,input().split())) for i in range(x)]

if x==1 and 1 in zido[0]:
    print(0)
    exit()
dpzido = [[-1 for i in range(y)] for i in range(x)]

fcnt = int(input())

forward = [list(map(int,input().split())) for i in range(fcnt)]

inqcnt = 0


for i in range(y):
    if zido[0][i]!=1:
        continue
    for j in range(fcnt):
        nextward = (0+forward[j][0],i+forward[j][1])
        #print(nextward)
        if nextward[0]<0 or nextward[1]<0: continue
        if nextward[0]>=x or nextward[1]>=y: continue
        if zido[nextward[0]][nextward[1]] != 1: continue
        #heapq.heappush(q,(1,nextward))
        q.append((1,nextward))
        inqcnt+=1


while True:
    if inqcnt<=0:
        print(-1)
        break
    inqcnt-=1
    #cnt, *nowpos = heapq.heappop(q)
    cnt, nowpos = q.popleft()
    #nowpos = nowpos[0]
    #print(cnt,nowpos)
    if nowpos[0]==x-1:
        print(cnt)
        break
    if dpzido[nowpos[0]][nowpos[1]] <= cnt and dpzido[nowpos[0]][nowpos[1]]!=-1:
        continue
    dpzido[nowpos[0]][nowpos[1]] = cnt
    for j in range(fcnt):
        nextward = (nowpos[0]+forward[j][0],nowpos[1]+forward[j][1])
        #print(nextward)
        if nextward[0]<0 or nextward[1]<0: continue
        if nextward[0]>=x or nextward[1]>=y: continue
        if zido[nextward[0]][nextward[1]] != 1: continue
        #heapq.heappush(q,(cnt+1,nextward))
        q.append((cnt+1,nextward))
        inqcnt+=1
        


        
        
