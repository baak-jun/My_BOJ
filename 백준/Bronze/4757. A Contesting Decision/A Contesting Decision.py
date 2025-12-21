msc = 999999999999999999999
ms = -1
t = ""
for i in range(int(input())):
    a, *b = input().split()
    sc = 0
    b = list(map(int,b))
    cnt = 0
    for j in range(4):
        if b[j*2+1]==0:
            continue
        else:
            cnt+=1
            sc+=b[j*2+1]
            sc+=(b[j*2]-1)*20
    #print(a,sc)
    if cnt>=ms and msc>=sc:
        
        msc = sc
        ms = cnt
        t = a
print(t,ms,msc)
            
            
    
