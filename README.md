# BOJ 문제 풀이 공간

[![Solved.ac
프로필](http://mazassumnida.wtf/api/v2/generate_badge?boj=1996yyk)](https://solved.ac/1996yyk)

<b>BaekJoon Quiz</b>

|Algorithm|Solved Problem|
|------|---|
|I&O|2557, 1000, 2558, 10950, 10951, 10952, 10953, 11021, 11022, 11718, 11719, 11720, 11721, 2741, 2742, 2739, 1924, 8393, 10818, 2438, 2439, 2440, 2441, 2442, 2445, 2522, 2446, 10991, 10992|
|DP|1463, 11726, 11727, 9095, 10844, 11057, 2193, 9465, 2156(거의 다품), 11053, 11055, 11722, 11054, 1912, 2579, 1699, 2133, 9461, 2225, 2011, 11052|
|ETC|2751, 11650, 11651, 10814, 10825, 10989, 11652, 11004, 10828, 9012, 10799, 10845, 10866, 10808, 10809, 10820, 2743, 11655, 10824, 11656, 1406, 1158, 1168, 10430, 2609, 1934, 1850, 9613, 11005, 2745, 1373, 1212, 2089, 11576, 1978, 1929, 6588, 11653, 10872, 1676, 2004,10821|
|GRAPH|1260, 11724, 1707, 10451, 2331, 9466, 2667, 4963, 7576, 2178 , 2146, 1991, 11725, 1167, 1967, 2606|
|BSTS|1654, 2805, 2110, 10815, 10816, 11662|
|DIVIDE&CONQUER|11728, 1780, 11729, 1992, 2447, 2448, 1517(잘 모르겠음), 2261(모르겠음)|
|GREEDY|11047, 2875, 10610, 1783, 1931, 11399, 2873, 1744|
|BRUTEFORCE|1476, 1107, 1451, 9095, 10819, 10971, 1697, 1963(잘모르겠다..), 9019, 1525(잘 모르겠음), 2251, 2186, 3108, 5014, 1759, 2580, 1987, 6603, 1182, 2003, 1806, 1644, 1261, 1208, 7453, 2632, 2143, 2557 |
|STRING|1181, 1316, 3029, 4659, 9046, 10798, 11365, 16171, 20154|
|IMPLEMENTATION|1244, 1913, 1996, 2072, 2578, 4386, 5597, 9093, 10994, 12933, 16926, 20053, 20291, 20546|

### 파이썬
* 2차원 배열 합
```python
sum(sum(board, []))
```
* 2차원 배열 90도 회전
```python
def rotate(board):
    return list(map(list, zip(*board[::-1])))
```
* 2차원 배열 행 열 뒤집기
```python
def flip(board):
    return list(map(list, zip(*board)))
```
* 정렬 key
```python
return [i[3] for i in sorted(answer, key=lambda x : (-x[0],-x[1], -x[2], x[3]))]
```
* 정규표현식
```python
import re

def solution(new_id):
    st = new_id
    st = re.sub('[^a-z0-9\-_.]', '', st.lower())
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = re.sub('[.]$', '', st[:15]) if len(st) else 'a'
    return st + ''.join([st[-1] for i in range(3-len(st))])
```
* 필터
```python
list(filter(lambda u: u["sex"] == 'M', users))

[user for user in users if user["sex"] == 'M']
```
* 이진탐색 - 오름차순으로 정렬된 리스트에서 특정한 값의 위치를 찾는 알고리즘
```python
import bisect
mylist = [1, 2, 3, 7, 9, 11, 33]
print(bisect.bisect(mylist, 3))
```
* 두 배열의 같은 자리 값을 합한 배열
```python
ret = [x + y for x, y in zip(a, b)]
```
* 이중 for문 한줄
```python
arr = []
for i in v:
    for j in i:
        arr.append(j)

arr = [j for i in v for j in i]
```
* 정규식 연속 중복 문자 제거
```python
import re


test = 'abbbsdfcdZZZZ11111)'
test0 = re.sub('(([a-zA-Z0-9])\\2*)', '', test) # 연속된 같은 문자 변환 (1개이상)
test1 = re.sub('(([a-zA-Z0-9])\\2+)', '', test) # 연속된 같은 문자 변환 (2개이상)
test2 = re.sub('(([a-zA-Z0-9])\\2{2,})', '', test) # 연속된 같은 문자 변환 (3개이상)
test3 = re.sub('(([a-zA-Z0-9])\\2{3,})', '', test) # 연속된 같은 문자 변환 (4개이상)
test4 = re.sub('(([a-zA-Z0-9])\\2{4,})', '', test) # 연속된 같은 문자 변환 (5개이상)

print(test1) 
print(test2)  
print(test3)
print(test4)

########결과########
asdfcd)
asdfcd)
abbbsdfcd)
abbbsdfcdZZZZ)

```

```python
def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] != [i]:
            a.append(i)
    return a 
```
```python
class LoopBreak(Exception):
    pass

try:
    for i in range(5):
        for j in range(5):
            if i == 1 and j == 1:
                raise LoopBreak()
except LoopBreak:
    pass
```
* 달팽이
```python
def solution(n, m, board):
    answer = [n // 2 + 1, n // 2 + 1]
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    y = x = n // 2
    num, length = 1, 0
    board[y][x] = num
    while y != -1 or x != -1:
        for d in range(4):
            for _ in range(length):
                y += dy[d]
                x += dx[d]
                num += 1
                board[y][x] = num
                if num == m:
                    answer = [y + 1, x + 1]
        y -= 1
        x -= 1
        length += 2
    return answer
```
