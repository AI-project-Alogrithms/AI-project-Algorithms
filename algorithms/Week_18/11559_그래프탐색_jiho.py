# Puyo Puyo
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

def under():
    arr_new = [['.']*6 for _ in range(12)]
    # for i in arr:
    #     print(i)
    # print("-----")
    for j in range(6):
        tlst = []
        for i in range(12):
            if arr[i][j] != '.':
                tlst.append(arr[i][j])
        # print("tlst: ", tlst)
        for i in range(11,11-len(tlst),-1):
            arr_new[i][j] = tlst.pop()
    # for i in arr_new:
    #     print(i)
    # print("-------")
    return arr_new

def remove(v):
    for i in range(12):
        for j in range(6):
            if v[i][j] == 1:
                arr[i][j] = '.'

def bfs(i,j):
    q = deque()
    q.append((i,j))
    v = [[0]*6 for _ in range(12)]
    v[i][j] = 1
    cnt =1 # 개수 세기
    color = arr[i][j]
    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1,0),(1,0),(0,1),(0,-1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<12 and 0<=nj<6 and v[ni][nj]==0 and arr[ni][nj]==color:
                v[ni][nj] = 1
                cnt+=1
                q.append((ni,nj))
    return cnt,v

arr = [list(input().rstrip()) for _ in range(12)]

# 4개 이상인거 찾기, 하나도 없으면 break
ans = 0
while(True):
    tmp = 0 # 하나도 없다면 멈추기
    for i in range(12):
        for j in range(6):
            if arr[i][j] != '.':
                cnt, v = bfs(i,j)
                if cnt >=4:
                    remove(v)
                    tmp+=1
    if tmp==0:
        print(ans)
        break
    arr=under()
    ans+=1

