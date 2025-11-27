import sys
def input():return sys.stdin.readline().rstrip()

a = int(input())

b = list(map(int,input().split()))


posa = 0
posb = a-1

ans = [-1000000000,-1000000000]
mins = 2000000001


for i in range(100000000):
    #print(posa,posb)
    if posa>=a or posb>=a:
        break
    if posb<=posa:
        break
    
    ka = b[posa]+b[posb]
    k = abs(ka)
    if k<mins:
        ans = (b[posa],b[posb])
        mins = k
    if ka<0:
        posa+=1

    else:
        posb-=1
    
    
    
    
        
        
print(*ans)
