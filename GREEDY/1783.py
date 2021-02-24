import sys
n,m = map(int,sys.stdin.readline().split())

# 세로가 1인경우 :: 어떤 이동방법도 못쓰는경우
if n == 1 :
    print(1)
# 세로가 2인경우 :: 2번 3번 방법만 사용하는경우
elif n == 2 :
    print(min(4,(m+1)//2))
# 세로가 3이상인 경우 ::
else :
    # 가로가 6 이하인 경우 :: 1번 4번 방법만 사용하는경우
    if m <= 6 :
        print(min(4,m))
    # 가로가 7 이상인 경우 :: 1,2,3,4번 모두 사용 가능
    else :
        print(m-2)
