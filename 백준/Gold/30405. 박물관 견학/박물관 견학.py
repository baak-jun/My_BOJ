import sys
def input():return sys.stdin.readline().rstrip()

a,b = map(int,input().split())

mus = []
for i in range(a):
    x,*k = map(int,input().split())
    mus.append(k[0])
    mus.append(k[-1])
print(sorted(mus)[a-1])
