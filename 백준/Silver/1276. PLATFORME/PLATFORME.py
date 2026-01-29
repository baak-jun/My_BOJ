import sys
def input():return sys.stdin.readline().rstrip()


zido = [0 for i in range(100001)]

su = 0

k = [list(map(int,input().split())) for i in range(int(input()))]

k = sorted(k)

for i in range(len(k)):
    h = k[i][0]
    j = k[i][1]
    z = k[i][2]-1
    su+= ((h*2)-zido[j]-zido[z])
    
    for x in range(j,z+1):
        zido[x]=h
    
print(su)
