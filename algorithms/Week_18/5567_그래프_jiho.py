# 결혼식
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

def bfs(me):
    q = deque(me)
    for x in me:
        v[x] = 1 # 방문 표시
    while q:
        cur = q.popleft()
        for next in arr[cur]:
            if v[next] == 0: # 미방문이면
                v[next] = 1
    return v.count(1)-1

n = int(input())
m = int(input())
arr=[[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
# print(arr)
v = [0]*(n+1)
v[1] = 1
print(bfs(arr[1]))