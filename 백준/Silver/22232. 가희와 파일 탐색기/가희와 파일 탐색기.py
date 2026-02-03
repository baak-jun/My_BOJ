import sys
def input():return sys.stdin.readline().rstrip()

a,b = map(int,input().split())

k = [input().split(".") for i in range(a)]

n = set([input() for i in range(b)])



k = sorted(k,key=lambda x:(x[0],x[1] not in n,x[1]))

for i in range(a):
    print(".".join(k[i]))
