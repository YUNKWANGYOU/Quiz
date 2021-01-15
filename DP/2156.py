N = int(input())

wine = []
for i in range(N) :
    wine.append(int(input()))

dp = [wine[0] + wine[1],wine[0] + wine[2],wine[1] + wine[2]]
cnt = 0

for i in range(3,N) :
    cnt += 1
    if cnt%3 == 1 :
        dp[0] = dp[0] + wine[i]
        dp[1] = dp[1] + wine[i]
    elif cnt%3 == 2 :
        dp[0] = dp[0] + wine[i]
        dp[2] = dp[2] + wine[i]
    elif cnt%3 == 0 :
        dp[1] = dp[1] + wine[i]
        dp[2] = dp[2] + wine[i]

print(max(dp))
