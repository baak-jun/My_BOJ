import sys
def input():return sys.stdin.readline().rstrip()

k = sorted(list(map(int,input().split())))

if k[0]+k[1]==k[2]:
    print(k[0],k[1],k[3])
else:
    print(k[0],k[1],k[2])

