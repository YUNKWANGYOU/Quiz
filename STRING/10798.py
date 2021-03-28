import sys
from collections import deque

q1 = deque(sys.stdin.readline().rstrip('\n'))
q2 = deque(sys.stdin.readline().rstrip('\n'))
q3 = deque(sys.stdin.readline().rstrip('\n'))
q4 = deque(sys.stdin.readline().rstrip('\n'))
q5 = deque(sys.stdin.readline().rstrip('\n'))
res = []

while 1 :
    if (not q1) and (not q2) and (not q3) and (not q4) and (not q5) :
        break
    try :
        res.append(q1.popleft())
    except:
        pass
    try :
        res.append(q2.popleft())
    except:
        pass
    try :
        res.append(q3.popleft())
    except:
        pass
    try :
        res.append(q4.popleft())
    except:
        pass
    try :
        res.append(q5.popleft())
    except:
        pass

for i in res :
    print(i,end='')
print()
