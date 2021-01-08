N = int(input())

a = input()

num = []

num.append(a.split(" "))
b = num[0]

b = list(map(int,b))

print(min(b),max(b))
