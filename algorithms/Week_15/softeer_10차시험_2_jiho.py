# 아마.. dfs, 완전 탐색 이용 문제 + 조합?
# 아무리 해도 l의 경로가 탐색으로 안찾아짐 이유가 뭔지 모르겠음.... ㅠㅠㅠㅠㅠㅠ

import sys
sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

di = [0,0,1,-1]
dj = [1,-1,0,0]

# def dfs(cnt,ci, cj,lst):
#     global all_list
#     if cnt == 5:
#         all_list.add(tuple(lst))  # 중복 방지를 위해 set에 tuple로 저장
#     for d in range(4):
#         ni, nj = ci+di[d], cj+dj[d]
#         if 0<=ni<n and 0<=nj<n and v[ni][nj]==0:
#             v[ni][nj] = 1 # 방문 표시
#             dfs(cnt+1, ni,nj,lst+[(ni,nj)])
#             v[ni][nj] = 0 # 탐색 후 방문 취소

def bfs():
    global all_list
    q = deque()

    # 모든 좌표에서 bfs탐색
    for i in range(n):
        for j in range(m):
            q.append((i,j,[(i,j)]))
            while(q):
                ci, cj, lst = q.popleft()
                if len(lst)==5:
                    all_list.add(tuple(lst))
                    continue
                for d in range(4):
                    ni,nj = ci+di[d], cj+dj[d]
                    if 0 <= ni < n and 0 <= nj < m and (ni, nj) not in lst:
                        q.append((ni, nj, lst + [(ni, nj)]))  # 새 좌표와 경로를 큐에 넣음


n,m = map(int, input().split()) # n,m = 3,4

v = [[0]*m for _ in range(n)]
all_list = set()
bfs()
# for i in range(n):
#     for j in range(m):
#         if v[i][j] == 0:
#             v[i][j] = 1
#             dfs(1,i,j,[(i,j)])
#             v[i][j] = 0
l = [(0,1),(1,0),(1,1),(2,1),(2,2)]

# for lst in all_list:
    # if frozenset(lst) == frozenset(l):  # 순서 상관없이 비교
    # if ((2, 2) and (2, 1) and (0, 1) and (1, 1) and (1, 0)) in lst:
    #     print(lst)
