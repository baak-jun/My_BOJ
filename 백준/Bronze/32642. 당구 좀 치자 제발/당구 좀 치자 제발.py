import sys
def input():return sys.stdin.readline().rstrip()

a = int(input())

b = list(map(int,input().split()))

rage = 0
ans = 0
for i in b:
    if i==0:
        rage-=1
    else:
        rage+=1
    ans+=rage
print(ans)
