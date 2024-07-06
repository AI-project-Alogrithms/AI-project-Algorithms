# 나이트의 이동 => bfs
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

def bfs(ci, cj):
    q = deque()
    q.append((ci, cj))
    arr[ci][cj] = 1
    while(q):
        ci, cj = q.popleft()
        for d in range(8):
            ni, nj = ci + di[d], cj + dj[d]
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 0:
                arr[ni][nj] = arr[ci][cj] + 1
                q.append((ni, nj))
                # print(arr)
    return (arr[fi][fj]-1)


T = int(input())
di = [-2,-2,-1,-1,1,1,2,2]
dj = [-1,1,-2,2,-2,2,-1,1]
for _ in range(T): # TEST CASE
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    ci, cj = map(int, input().split())
    fi, fj = map(int, input().split())
    # visited = [[0]*N for _ in range(N)]
    print(bfs(ci, cj))