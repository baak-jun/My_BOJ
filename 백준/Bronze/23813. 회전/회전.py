a = list(input())
ans = 0
for i in range(len(a)):
    ans+=int("".join(a))
    a.append(a.pop(0))
print(ans)

