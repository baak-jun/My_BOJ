import sys
def input():return sys.stdin.readline().rstrip()

a = int(input())

b = int(input())

cnt = 2
now = 0

nowlen = a
while True:
    
    nowlen = nowlen*b//100
    #print(nowlen)
    if nowlen<=5:
        break
    now += nowlen*cnt
    cnt*=2
    
    
    
print(now)
