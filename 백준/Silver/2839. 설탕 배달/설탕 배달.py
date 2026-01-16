import sys
def input():return sys.stdin.readline().rstrip()

a = int(input())
ans = 0

if a==4 or a==7:
    print(-1)
    exit()
while True:
    if a<3:
        print(-1)
        break
    elif a%5==0:
        print(a//5+ans)
        break
    elif a%3==0 and a>=15:
        ans +=3
        a -= 15
    elif a%3==0:
        print(a//3+ans)
        break
    else:
        a-=5
        ans+=1
        
        
