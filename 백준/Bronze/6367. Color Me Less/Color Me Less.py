import sys
def input():return sys.stdin.readline().rstrip()


a = set(tuple(map(int,input().split())) for i in range(16))


while True:
    k = list(map(int,input().split()))
    if k[0]==-1:
        break
    last = (-1,-1,-1)
    mdis = 99999999999
    for i in a:
        temp = (k[0]-i[0])**2+(k[1]-i[1])**2+(k[2]-i[2])**2
        if temp<mdis:
            last = i
            mdis = temp
    print(f"({k[0]},{k[1]},{k[2]}) maps to ({last[0]},{last[1]},{last[2]})")
