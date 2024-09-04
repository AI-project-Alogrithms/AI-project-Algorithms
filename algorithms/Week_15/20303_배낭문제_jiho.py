# 할로원의 양아치
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

def neaps(lst):
    lst = [(0,0)]+lst
    # print(lst)
    dp = [[0]*K for _ in range(len(lst))]
    # print(len(dp))
    for i in range(1,len(lst)):
        for j in range(1,K):
            if lst[i][0]>j:
                dp[i][j] = dp[i-1][j]
            else:
                # print(lst[i][0], lst[i][1])
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-lst[i][0]] + lst[i][1])
    return dp[-1][-1]


def bfs(node):

    q = deque(arr[node])
    cnt, candy = 1, lst[node]
    while q:
        nextnode = q.popleft()
        if not visited[nextnode]:
            visited[nextnode] = True
            cnt +=1
            candy += lst[nextnode]
            if arr[nextnode]:
                for n in arr[nextnode]:
                    q.append(n)
    # print(cnt, candy)
    return cnt, candy


N, M, K = map(int, input().split())
lst = [0]+list(map(int, input().split()))
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
# print(arr)
visited = [False]*(N+1)
anslst = []
for i in range(1,N+1):
    if visited[i]==False:
        visited[i] = True
        cnt, candy =bfs(i)
        anslst.append((cnt, candy))
# print(anslst)
print(neaps(anslst))

