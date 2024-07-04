# ABCDE
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def dfs(root,cnt, visited):
    if cnt == 4:
        return True
    visited[root] = True
    for i in tree[root]:
        if not visited[i]:
            if dfs(i,cnt+1,visited):
                return True
    visited[root] = False
    return False


N, M = map(int, input().split())
tree = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
print(tree)

visited = [False]*N
for i in range(N):
    visited = [False] * N
    if dfs(i, 0, visited) == True:
        ans = 1
        break
    ans = 0

print(ans)