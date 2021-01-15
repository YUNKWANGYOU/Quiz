a = int(input())

dp = [[0 for i in range(10)] for j in range(101)]
dp[1] = [0,1,1,1,1,1,1,1,1,1]

for i in range(2,a+1) :
    for j in range(0,10) :
        if j == 0 :
            dp[i][j] = dp[i-1][j+1]
        elif j == 9 :
            dp[i][j] = dp[i-1][j-1]
        else :
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
print(sum(dp[a])%1000000000)
