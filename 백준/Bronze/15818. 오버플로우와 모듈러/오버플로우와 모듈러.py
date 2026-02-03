import sys
def input():return sys.stdin.readline().rstrip()

a,b = map(int,input().split())

k = list(map(int,input().split()))

su = 1
for i in k:
    su*=i
    su%=b
print(su)
