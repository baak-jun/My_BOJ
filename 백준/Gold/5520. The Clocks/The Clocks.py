import sys
def input():return sys.stdin.readline().rstrip()
sync = [(0,1,3,4),
        (0,1,2),
        (1,2,4,5),
        (0,3,6),
        (1,3,4,5,7),
        (2,5,8),
        (3,4,6,7),
        (6,7,8),
        (4,5,7,8)]

ans = [12 for i in range(16)]
sol = []
rans = []

#clock = list(map(int,input().split()))
mcnt = 999999999999

clock = [list(map(int,input().split())) for i in range(3)]

clock = [*clock[0],*clock[1],*clock[2]]


for a1 in range(4):
    for a2 in range(4):
        for a3 in range(4):
            for a4 in range(4):
                for a5 in range(4):
                    for a6 in range(4):
                        for a7 in range(4):
                            for a8 in range(4):
                                for a9 in range(4):
                                    
                                    ck = clock[:]
                                    k = [a1,a2,a3,a4,a5,a6,a7,a8,a9]
                                    nowans = []
                                    
                                    for j in range(9):
                                        for x in range(k[j]):
                                            nowans.append(j)
                                            for z in sync[j]:
                                                ck[z] = (ck[z]+1)%4
                                                    

                                        
                                    if all(x == 0 for x in ck):
                                        #print(k)
                                        zy = sum(k)
                                        if mcnt>zy:
                                            mcnt = zy
                                            sol = nowans
for j in sol:
    print(j+1,end=" ")

                
