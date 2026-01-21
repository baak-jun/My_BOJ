import sys
def input():return sys.stdin.readline().rstrip()


a = input()

x,y = map(int,input().split())
k = len(a)

zido = [input() for i in range(x)]


for i in range(x):
    #오른쪽,왼쪽
    if a in zido[i] or (a[::-1] in zido[i]):
        print(1)
        exit()
    for j in range(y):
        #오른쪽 아래 대각선, 왼쪽 위 대각선
        if j+k<=y and i+k<=x:
            temp = []
            for z in range(k):
                temp.append(zido[i+z][j+z])
            temp = "".join(temp)
            if temp==a or temp[::-1]==a:
                print(1)
                exit()
        #아래, 위
        if i+k<=x:
            temp = []
            for z in range(k):
                temp.append(zido[i+z][j])
            temp = "".join(temp)
            if temp==a or temp[::-1]==a:
                print(1)
                exit()

        #왼쪽 아래, 오른쪽 위
        if j+k<=y and i-k>=0:
            temp = []
            for z in range(k):
                temp.append(zido[i-z][j+z])
            temp = "".join(temp)
            if temp==a or temp[::-1]==a:
                print(1)
                exit()
else:
    print(0)
