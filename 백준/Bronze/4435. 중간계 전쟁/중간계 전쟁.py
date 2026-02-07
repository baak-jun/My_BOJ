import sys
def input():return sys.stdin.readline().rstrip()

gan = [1,2,3,3,4,10]

sa = [1,2,2,2,3,5,10]


for i in range(int(input())):
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    gancnt = 0
    sacnt = 0
    for j in range(6):

        gancnt+=a[j]*gan[j]
    for j in range(7):
        sacnt+= b[j]*sa[j]
    if gancnt<sacnt:
        print(f"Battle {i+1}: Evil eradicates all trace of Good")
    elif gancnt>sacnt:
        print(f"Battle {i+1}: Good triumphs over Evil")
    else:
        print(f"Battle {i+1}: No victor on this battle field")
