# 트리의 지름 => 처음에 시간초과, 힌트 봄 => 두번의 dfs로도 가능..
# step1. 임의의 노드에서 dfs 수행해서 가장 먼 노드 far_node찾기
# step2. 찾은 far_node에서 다시 dfs 수행해서 트리의 지름 계산하기
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def dfs(node,cnt):
    global max_cnt, far_node
    if max_cnt<cnt:
        max_cnt = cnt
        far_node = node
    visited[node] = 1
    for n, v in arr[node]:
        if visited[n] == 0:
            dfs(n, cnt+v)
    return


N= int(input())
arr = [[] for _ in range(N+1)]
for _ in range(N):
    a = list(map(int, input().split()))
    for i in range(1,len(a)-1,2):
        arr[a[0]].append([a[i],a[i+1]])
# print(arr)
visited = [0]*(N+1)
max_cnt = 0
# 가장 먼 노드 찾기
far_node = 0
dfs(1,0)

visited = [0]*(N+1)
max_cnt = 0
dfs(far_node,0)
# for i in range(1,N+1):
#     if visited[i] == 0:
#         visited[i]=1
#         dfs(i,0)
#         visited[i]=0
print(max_cnt)