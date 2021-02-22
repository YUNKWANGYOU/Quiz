#메모리초과
import sys
sys.setrecursionlimit(10**9)

def distance(x1,x2) :
    return((x2[0]-x1[0])**2 + (x2[1]-x1[1])**2)

def short_length(start,end) :
    length = end - start
    if length == 2 :
        return distance(arr[start],arr[start+1])
    elif length == 3 :
        return min(distance(arr[start],arr[start+1]),distance(arr[start],arr[start+2]),distance(arr[start+2],arr[start+1]))
    else :
        mid = (start + end)//2
        d = min(short_length(start,mid),short_length(mid,end))

        middle = arr[mid][0]
        tmp_list = []

        for i in range(start, end) :
            if(arr[i][0] - middle)**2 <= d :
                tmp_list.append(arr[i])

        tmp_len = len(tmp_list)
        if tmp_len >= 2 :
            tmp_list.sort(key = lambda x : x[1])
            for i in range(tmp_len - 1) :
                for j in range(i+1, tmp_len) :
                    if(tmp_list[i][1] - tmp_list[j][1]) ** 2 > d :
                        break
                    elif tmp_list[i][0] < middle and tmp_list[j][0] < middle :
                        continue
                    elif tmp_list[i][0] >= middle and tmp_list[j][0] >= middle :
                        continue

                    d = min(d,distance(tmp_list[i],tmp_list[j]))

        return d

n = int(sys.stdin.readline())
arr = list(set(tuple(map(int, input().split())) for _ in range(n)))
arr.sort(key = lambda x :x[0])
if n != len(arr) :
    print(0)
else :
    print(short_length(0,n))
