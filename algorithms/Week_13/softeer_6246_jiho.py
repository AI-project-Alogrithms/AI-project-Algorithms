# 순서대로 방문하기
import sys
sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from itertools import product

di = [0,0,-1,1]
dj = [-1,1,0,0]

def dfs(path, cnt):
    global route
    if cnt == m:  # end에 도착했다면
        # print("path: ", path)
        route.append(path) # 경로 넣기
        return

    if (path[-1] == lst[cnt]):
        dfs(path, cnt+1)
        return

    for i in range(4):
        ni, nj = path[-1][0]+di[i], path[-1][1]+dj[i]
        if 0<=ni<n and 0<=nj<n and arr[ni][nj]==0 and (ni, nj) not in path:
            dfs(path +[[ni, nj]], cnt)

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
lst = []
# dp = [[0]*n for _ in range(n)]
route = [] # 경로 저장
for _ in range(m):
    x, y = map(int, input().split())
    lst.append([x-1, y-1])
dfs([lst[0]],0) # 경로 저장, 경로 가기
print(len(route))

#
# # s -> e까지 가는 모든 경우의 수 구하기
# all_path = []
# for i in range(m-1):
#     route = [] # 경로 저장
#     si, sj = lst[i][0], lst[i][1]
#     ei, ej = lst[i+1][0], lst[i+1][1]
#     dp[si][sj] = 1
#     dfs([(si,sj)], si, sj)
#     # print(route)
#     all_path.append(route)
# # print(len(all_path))
# # print("all_path: ", all_path)
#
# # 모든 조합 구하기
# cnt = 0
# for comb in product(*all_path):
#     cnt += true_path(comb)
# print(cnt)