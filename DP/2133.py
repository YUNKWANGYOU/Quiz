a = int(input())

dp = [0 for i in range(31)]

dp[2] = 3

for i in range(4,a+1,2) :
    dp[i] = 3*dp[i-2] + 2*sum(dp[:i-2]) + 2

if a % 2 == 1 :
    print(0)
else :
    print(dp[a])
