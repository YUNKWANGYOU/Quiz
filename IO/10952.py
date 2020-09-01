d = []
cnt = 0

while True:

    try:
        a, b = input().split()
        c = int(a) + int(b)
        d.append(c)
        cnt += 1
        if a == "0" and b == "0":
            cnt -= 1
            break

    except:
        break

for k in range(0, cnt):
    print(d[k])