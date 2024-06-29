# 차이를 최대로
import sys
# sys.setrecursionlimit(5000)
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def dfs(n, ans):
    global max_v, visited
    if n==N:
        # print(ans)
        result = 0
        for i in range(1,N):
            result += abs(ans[i-1]-ans[i])
            # print(result)
        max_v = max(max_v, result)
        return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            # 같은 수가 있을 수 있음, 따라서 해당 배열값을 방문 했는지로 확인하기
            dfs(n+1, ans+[arr[i]])
            visited[i] = 0
N = int(input())
arr = list(map(int, input().split()))
arr.sort()
# print(arr)
max_v = 0
visited = [0] * N
dfs(0, [])
print(max_v)