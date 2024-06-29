# 효도여행
import sys
sys.setrecursionlimit(5000)
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def dfs(cur,length,st): # 현재 노드, 탐색 깊이, 현재까지의 문자열 st
    global ans
    visited[cur] = True # 현재 노드 방문 표시
    # print("문자열 비교")
    # print(st, S)
    # LCS 구하기 (예전에 한거 기억난다...!)
    for cursor in range(M+1): # 문자열의 길이만큼 반복
        # print("cursor: ", cursor)
        if length == 0 or cursor == 0: # dp 초기 조건
            dp[length][cursor] = 0
            # print("초기조건: ", length, cursor, dp)
        elif st[length-1] == S[cursor - 1]: # 문자가 일치하는 경우 이전값 +1,
            # print(st[length - 1], S[cursor - 1])
            dp[length][cursor] = dp[length-1][cursor - 1] + 1
            # print("dp 갱신: ", dp)
        else: # 문자가 일치하지 않은 경우 이전 값중 최대값
            dp[length][cursor] = max(dp[length - 1][cursor], dp[length][cursor - 1])
            # print("dp 이전값 중 최댓 값: ", dp)
        ans = max(ans, dp[length][cursor])
    for edge in edges[cur]:
        # print(edge)
        ne, nch = edge
        if visited[ne] == True:
            continue
        dfs(ne, length +1, st+nch)






# 정점의 개수, 문자열의 길이
N, M = map(int, input().split())
S = input().rstrip() # 문자열 S
# print(S)
# graph = [[] for _ in range(N+1)]
# print(graph)


edges = [[] for _ in range(5005)] # 각 노드 인접리스트
dp = [[0]*5005 for _ in range(5005)] # dp[length][cursor] 누적된 최대 일자
visited = [False] * 5005
ans = 0

for _ in range(N-1):
    u, v, c = map(str, input().rstrip().split())
    edges[int(u)].append((int(v),c))
    edges[int(v)].append((int(u),c))
# print(edges)

dfs(1, 0, "") # 현재노드, 길이, 문자열
print(ans)
