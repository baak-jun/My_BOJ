import sys
def input():return sys.stdin.readline().rstrip()


a = int(input())
b = list(map(int,input().split()))

mscore = 0

mjo = (0,0)

for i in range(10000001):
    temp = a-b[1]*i
    if temp<0:
        break
    jo = (i,temp//b[3])
    score = temp//b[3]*b[2]+b[0]*i

    if mscore<score:
        mjo = jo
        mscore = score
print(*mjo)
    
