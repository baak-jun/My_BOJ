import sys
def input(): return sys.stdin.readline().strip()
a,b = map(int,input().split())

k = sorted([int(input()) for i in range(a)])

lp = 1

rp = 2999999999

ans = -1

ansc = -1
while True:
    cnt = 0
    if lp>=rp:
        break
    #print(lp,rp)
    x = (lp+rp)//2

    for i in k:
        cnt+=i//x
    if b<= cnt and cnt>0:
        ans = x
        ansc = cnt
        lp = x+1
    else:
        rp = x
print(ans)


