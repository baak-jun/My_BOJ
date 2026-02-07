import sys
def input():return sys.stdin.readline().rstrip()

a = int(input())

x = []
y = 0

for i in range(a):
    q,w = map(int,input().split())
    x.append(q)
    y+= w

x = sorted(x)

k = [(i+1)*j for i,j in enumerate(x)]
#print(k)

print(sum(k)+y)
