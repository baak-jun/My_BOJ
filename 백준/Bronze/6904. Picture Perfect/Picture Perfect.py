import sys
def input():return sys.stdin.readline().rstrip()


while True:
    a = int(input())

    if a==0:
        break
    mp = -1
    mpos = (-1,-1)
    for i in range(1, a+1):
        
        if a%i!=0:
            continue
        
        if mp==-1:
            mp = 2*i+(a//i)*2
            mpos = (min(i,a//i),max(i,a//i))
        elif mp>2*i+(a//i)*2:
            mp = 2*i+(a//i)*2
            mpos = (min(i,a//i),max(i,a//i))
    print(f"Minimum perimeter is {mp} with dimensions {mpos[0]} x {mpos[1]}")  
        
