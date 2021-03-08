import sys

n,s = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))

sum = [0]*(n+1)
for i in range(1,n+1) :
    sum[i] = sum[i-1]+a[i-1]

res = 1000001
start = 0
end = 1

while start != n :
    if sum[end] - sum[start] >= s :
        #길이가 제일 짧은 결과를 저장해놓기
        if end - start < res :
            res = end - start
        start +=1
    else :
        #0부터 end까지 탐색
        if end == n :
            start+=1
        #start부터 n까지 탐색
        else :
            end+=1

if res != 1000001 :
    print(res)
else :
    print(0)
