N  = int(input())

a =list(map(int,input().split(" ")))

dp = [0 for i in range(N)]



for i in range(N) :
    sum = []
    for j in range(i-1,-1,-1) :
        if a[i] > a[j] :
            sum.append(dp[j])

    if not sum :
        dp[i] = a[i]
    else :
        dp[i] = a[i] + max(sum)



print(max(dp))
