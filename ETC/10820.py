import sys

s_list = []

s_l = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s_s = "abcdefghijklmnopqrstuvwxyz"
s_n = "0123456789"
s_nl = " "

cnt_l = 0
cnt_s = 0
cnt_n = 0
cnt_nl = 0

while 1 :

    s = sys.stdin.readline().rstrip('\n')

    if s == '' :
        break
    else :
        s_list.append(s)

for i in range(len(s_list)) :
    for j in range(len(s_list[i])) :
        if s_list[i][j] in s_l :
            cnt_l += 1
        elif s_list[i][j] in s_s :
            cnt_s += 1
        elif s_list[i][j] in s_n :
            cnt_n += 1
        elif s_list[i][j] in s_nl :
            cnt_nl += 1
        else :
            pass

    print(cnt_s,cnt_l,cnt_n,cnt_nl)
    cnt_l = 0
    cnt_s = 0
    cnt_n = 0
    cnt_nl = 0
