a = list(map(int,input()))
dp = [0 for _ in range(len(a) + 1)]
dp[0] = 1

for i in range(0, len(a)) :

    if a[i] >= 1 and a[i] <=9 :
        dp[i+1] += dp[i]
        
    if i == 0 :
        continue

    now = a[i-1]*10 + a[i]

    if now >= 10 and now <= 26 :
        dp[i+1] += dp[i-1]

print(dp[len(a)] % 1000000)
