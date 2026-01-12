import sys
def input():return sys.stdin.readline().rstrip()

a = input()
b = input()


for i in range(len(a)):
    if a[i]==" ":
        print(" ",end="")
    else:
        print(chr(ord("a")+((26+ord(a[i])-ord("a") -1- (ord(b[i%len(b)])-ord("a"))))%26),end="")
    
    

        
