import sys
def input():return sys.stdin.readline().rstrip()

a = int(input())

b = input().split()

bcnt = b.count("1")


c = input().split()
ccnt = c.count("1")



#print(bcnt,ccnt)

cnt = 0

for i in range(a):
    if b[i]!=c[i]:
        cnt+=1

#print(cnt)

if "1" in b:
    #토글,전체체크+토글,전체체크+전체해제+토글
    
    if "0" not in b:
        #이미 전체토글이면 전체체크는 안해도 됨
        print(min(cnt,a-ccnt,1+ccnt))
        exit()
    print(min(cnt,1+a-ccnt,2+ccnt))
else:
    #토글, 아무거나+전체체크+토글, 아무거나+전체체크+전체해제+토글
    print(min(cnt,1+a-ccnt,ccnt))
