a = input()
k = len(a)

j = k//3

z = [a[:j],a[j:2*j],a[2*j:]]

x = set(z)

if len(x)==1:
    print(z[0])
else:
    k = list(x)
    if z.count(k[0])==2:
        print(k[0])
    else:
        print(k[1])
