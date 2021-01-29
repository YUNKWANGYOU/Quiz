import sys

l_stack = list(sys.stdin.readline().rstrip('\n'))
r_stack = list()

n = int(sys.stdin.readline())

for i in range(n) :
    command = sys.stdin.readline()
    if command[0] == 'L' and l_stack :
        r_stack.append(l_stack.pop())
    elif command[0] == 'D' and r_stack :
        l_stack.append(r_stack.pop())
    elif command[0] == 'B' and l_stack :
        l_stack.pop()
    if command[0] == 'P' :
        l_stack.append(command[2])

for i in range(len(l_stack)) :
    print(l_stack[i],end = '')
for i in range(len(r_stack)-1,-1,-1) :
    print(r_stack[i],end = '')

print("")
