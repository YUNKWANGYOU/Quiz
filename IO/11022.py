n = input()

sum = []
A = []
B = []

for i in range(int(n)) :

    try:
        a,b = input().split(" ")
        A.append(a)
        B.append(b)

    except :
        break

    c = int(a) + int(b)

    sum.append(c)


for i in range(int(n)) :
     print("Case #"+str(i+1)+": " + str(A[i]) + " + " + str(B[i]) + " = "+ str(sum[i]))
