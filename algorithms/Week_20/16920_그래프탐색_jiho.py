# 확장게임 => 다시 풀기
import sys
sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

di = [0,0,1,-1]
dj = [1,-1,0,0]

def bfs(lst, key):
    global cnt
    q = deque(lst)
    # c = kanlst[key]*len(lst)
    c = len(lst)
    kan = kanlst[key]
    while(q):

        c-=1
        if c==0:
            kan-=1
            c = len(q)
            if kan<0:
                return q
        ci, cj = q.popleft()
        for dr in range(4):
            ni, nj = ci+di[dr], cj+dj[dr]
            if 0<=ni<N and 0<=nj<M and arr[ni][nj]=='.':
                arr[ni][nj]=key
                cnt-=1
                q.append((ni, nj))





N, M, P = map(int, input().split())
kanlst = [0]+list(map(int, input().split()))
print(kanlst)
# visited = [[False]*M
arr = [list(input().rstrip()) for _ in range(N)]
lst = []
dict = {}
cnt=0
for i in range(N):
    for j in range(M):
        if arr[i][j]!='.':
            k = int(arr[i][j])
            if k not in dict:
                dict[k] = []
            dict[k].append((i,j))
            # print(k)
            arr[i][j] = k
            # lst.append((k, i, j, kanlst[k]))
        elif arr[i][j]=='.':
            cnt+=1
# lst.sort()
print(dict)
print(cnt)
while(True): # 빈칸이 있을 동안
    for key, value in dict.items():
        # for i in range(kanlst[key]):
        v=bfs(value, key)
        dict[key] = v
    if cnt==0:
        break
    # arrs = sum(arr, [])
    # if arrs.count('.')==0:break
    # print(arrs.count(0))

for i in arr:
    print(i)
arrs = sum(arr,[])
print(arrs)
for i in range(1,P+1):
    print(arrs.count(i), end=" ")
# bfs(lst)


