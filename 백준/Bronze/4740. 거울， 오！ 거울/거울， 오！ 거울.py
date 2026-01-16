ans = []
while True:
    a = input()
    if a=="***":
        break
    ans.append(a[::-1])

print(*ans,sep="\n",end="")