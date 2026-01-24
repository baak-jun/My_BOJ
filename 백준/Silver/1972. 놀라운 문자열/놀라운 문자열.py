import sys
def input():return sys.stdin.readline().rstrip()

while True:
    a = input()
    if a=="*":
        break

    

    al = len(a)
    flag = 0
    for i in range(al-2):
        dic = dict()
        for j in range(al-i-1):
            temp = a[j]+a[j+i+1]
            if temp in dic:
                flag = 1
                break
            else:
                dic[temp] = 1
        if flag==1:
            print(f"{a} is NOT surprising.")
            break
    else:
        print(f"{a} is surprising.")
    
