a = int(input())
co = 0
if a==4 or a==7:
    print(-1)
    exit()
while True:

    if a%5==0:
        print(co+a//5)
        break
    elif (a//3>=5 and a%3==0):
        a =a-15
        co = co+3
    elif a%5 != 0 and a>=5 and a%3!=0:
        a = a-5
        co = co+1
    else:
        print(co+a//3)
        break
        
