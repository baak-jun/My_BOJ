a = input()
k = 0
su = 0
for i in range(len(a)):
    if(a[i]=="*"):
        k = i
        continue
    if(i%2==0):
        su+=int(a[i])
    else:
        su+=(int(a[i])*3)

su %=10
if su==0:
    print(0)
elif k%2==0:
    print(10-su)
else:
    print((10-su)*7%10)
    
