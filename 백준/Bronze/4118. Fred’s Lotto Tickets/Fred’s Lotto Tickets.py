


while True:
    a = int(input())
    if a==0:
        break
    k = [input().split() for i in range(a)]

    ch = [0 for i in range(49)]
    for j in k:
        for i in j:
            ch[int(i)-1]=1
    #print(ch)
    if 0 in ch:
        print("No")
    else:
        print("Yes")

