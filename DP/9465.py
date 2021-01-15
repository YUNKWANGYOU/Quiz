T = int(input())

for i in range(T):
    dp = []
    n = int(input())

    for j in range (0, 2) :
        dp.append(list(map(int,input().split(" "))))

    dp[1][1] =  dp[1][1] + dp[0][0]
    dp[0][1] =  dp[0][1] + dp[1][0]

    for k in range (2,n) :
        dp[0][k] = dp[0][k] + max(dp[1][k-1],dp[1][k-2])
        dp[1][k] = dp[1][k] + max(dp[0][k-1],dp[0][k-2])

    print(max(dp[0][n-1],dp[1][n-1]))
