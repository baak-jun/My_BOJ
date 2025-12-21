for i in range(int(input())):
    a = input()
    last = ""
    for i in range(len(a)):
        if last!=a[i]:
            print(a[i],end="")
            last=a[i]


    print()