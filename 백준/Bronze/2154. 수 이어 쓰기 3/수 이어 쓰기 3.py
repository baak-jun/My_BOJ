a = input()

k = []

for i in range(1,100003):
    k.append(str(i))
k = "".join(k)

al = len(a)

for i in range(10000001):
    if a==k[i:i+al]:
        print(i+1)
        break
