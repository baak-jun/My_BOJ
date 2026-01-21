import sys
def input():return sys.stdin.readline().rstrip()
a = int(input())

dp = [-1 for i in range(16)]
dp[0] = 1
dp[1] = 2
dp[2] = 6
dp[3] = 18

dpex = [-1 for i in range(16)]

dpex[0] = 0
dpex[1] = 0
dpex[2] = 1
dpex[3] = 3

for i in range(3,16):
    dpex[i] = dpex[i-1]+dp[i-2]
    dp[i] = dp[i-1]*2+dpex[i]*2



print(dp[a])
