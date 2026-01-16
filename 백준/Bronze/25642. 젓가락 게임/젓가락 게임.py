a = list(map(int,input().split()))

ans = ["yt","yj"]

for i in range(10):
    if a[0]>=5 or a[1]>=5:
        break
    a[(i+1)%2] += a[i%2]
print(ans[a.index(min(a))])
