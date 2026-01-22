import sys
def input():return sys.stdin.readline().rstrip()
from collections import deque


def dele(c):
    return c%7

n,m = map(int,input().split())


a = list(map(int,input().split()))

coa = sorted(set(list(map(dele,a))))
xk = len(coa)
dic = dict()

for i,j in enumerate(coa):
    dic[str(j)] = i

#print(xk,end = "\n\n")
nomal = coa



b = list(map(int,input().split()))

check = [0 for i in range(xk)]
cnt = 0
k = 0

theN = 10**9+7

for i in range(m):
    temp = []
    for j in range(xk):
        temp.append(nomal[j] + b[i])
        if temp[j]%7==0 and check[j]==0:
            cnt+=1
            if xk<=cnt:
                cnt-=1
                break
            check[j] = 1
    else:
        k+=b[i]
        nomal = temp

#print(check)
#print(nomal)
cnt = 0
ans = []

for i in range(n):
    temp = a[i]+k
    if check[dic[str(a[i]%7)]]==0:
        ans.append(temp%theN)
        cnt+=1
print(cnt)
print(*ans,sep=" ")
        
        
