a = int(input())

dp = [[0 for i in range(10)] for j in range(1001)]
dp[1] = [1,1,1,1,1,1,1,1,1,1]

for i in range(2,1001) :
    for j in range(0,10) :
        for k in range(0,j+1):
            dp[i][j] = dp[i][j] + dp[i-1][k]
print(sum(dp[a])%10007)
print(dp[3])
