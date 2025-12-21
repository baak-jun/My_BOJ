a= int(input())

for i in range(a):

    
    print(i+1,end = " ")
    if (i+1)%6==0:
        print("Go!",end=" ")

if a%6!=0:
    print("Go!",end="")
