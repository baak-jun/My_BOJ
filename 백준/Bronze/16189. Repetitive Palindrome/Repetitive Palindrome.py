import sys
def input():return sys.stdin.readline().rstrip()

a = input()

b = int(input())%2+1

a = a*b

    
if a==a[::-1]:
    print("YES")
else:
    
    print("NO")
    
