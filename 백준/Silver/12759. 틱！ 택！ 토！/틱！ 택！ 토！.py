import sys
def input():return sys.stdin.readline().rstrip()

player = ["o","x"]

a = int(input())

zido = [["" for i in range(3)] for i in range(3)]


def check():
    #옆으로
    for i in range(3):
        if zido[i]==["o","o","o"]:
            return 1
        elif zido[i]==["x","x","x"]:
            return 2

    #오른대각선
    if zido[0][0]=="o" and zido[0][0]==zido[1][1] and zido[2][2]==zido[0][0]:
        return 1
    elif zido[0][0]=="x" and zido[0][0]==zido[1][1] and zido[2][2]==zido[0][0]:
        return 2
    #왼대각선
    if zido[0][2]=="o" and zido[0][2]==zido[1][1] and zido[2][0]==zido[0][2]:
        return 1
    elif zido[0][2]=="x" and zido[0][2]==zido[1][1] and zido[2][0]==zido[0][2]:
        return 2
    #위로
    for i in range(3):
        if zido[0][i]=="o"and zido[0][i]==zido[1][i] and zido[0][i]==zido[2][i]:
            return 1
        elif zido[0][i]=="x"and zido[0][i]==zido[1][i] and zido[0][i]==zido[2][i]:
            return 2
            
    return 0
turn = (a+1)%2
for i in range(9):
    x,y = map(int,input().split())
    zido[x-1][y-1] = player[turn]
    #print(turn)
    
    turn = (turn+1)%2
    
    k = check()
    if k!=0:
        print(k)
        break

else:
    print(0)
