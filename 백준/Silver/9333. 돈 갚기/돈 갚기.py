import sys
def input():return sys.stdin.readline().rstrip()

a = int(input())

for i in range(a):
    r,b,m = map(float,input().split())
    b = int(b*100+0.5)
    m = int(m*100+0.5)
    r = int(r*100+0.5)
    start = b
    for j in range(1200):
        k = (b*r+5000)//10000
        b += k
        b-=m
        
        if b<=0:
            print(j+1)
            break
        if start<b:
            print('impossible')
            break
        #print(b)
    else:
        print('impossible')
        
