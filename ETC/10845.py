import sys

n = int(sys.stdin.readline())

list = []

for _ in range(n) :

    command = sys.stdin.readline()

    if command.split()[0] == 'push' and len(command.split()) == 1 :
        print("스택에 넣으실 숫자를 입력해주세요.")

    if command.split()[0] == 'push' and len(command.split()) == 2 :
        list.append(command.split()[1])
    elif command.split()[0] == 'pop' :
        try :
            data = list[0]
            del list[0]
            print(data)
        except :
            print(-1)
    elif command.split()[0] == 'size' :
        print(len(list))
    elif command.split()[0] == 'empty' :
        if bool(list) :
            print(0)
        else :
            print(1)
    elif command.split()[0] == 'back' :
        try :
            print(list[len(list)-1])
        except :
            print(-1)
    elif command.split()[0] == 'front' :
        try :
            print(list[0])
        except :
            print(-1)
    else :
        break
