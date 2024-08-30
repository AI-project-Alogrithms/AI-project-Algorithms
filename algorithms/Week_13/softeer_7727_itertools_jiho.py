# 함께하는 효도
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from itertools import product

di = [0,0,-1,1]
dj = [-1,1,0,0]

def dfs(path, ci, cj):
    global f_route
    if len(path)==4: # 3초가 지났으면
        f_route.append(path[:]) # 경로 추가
        return
    for i in range(4):
        ni, nj = ci+di[i], cj+dj[i]
        if 0<=ni<n and 0<= nj<n and (ni,nj) not in path: # 아직 미방문
            path.append((ni,nj))
            dfs(path, ni, nj)
            path.pop()

def total_sum(comb):
    # comb = ([(0, 1), (0, 0), (1, 0), (1, 1)], [(1, 2), (1, 1), (0, 1), (0, 2)])
    cnt=0
    visited = set()
    for route in comb:
        # print("route: ", route)
        for ci, cj in route:
            if (ci, cj) in visited: return 0 # 겹치는 경로가 있다면 과일 수집 안함
            visited.add((ci,cj)) # 경로 수집
            # print("visited:", visited)
            cnt+=arr[ci][cj]
    return cnt


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
friend = []
for _ in range(m):
    x, y = map(int, input().split())
    friend.append((x-1,y-1))

# 갈수있는 전체 경로 찾기
all_path = []
for i in range(m):
    # print("i: ", i)
    f_route = []
    dfs([friend[i]], friend[i][0], friend[i][1])
    # print(f_route)
    all_path.append(f_route)

# 가능한 모든 경로 조합 중 최대 과일 수 찾기
ans = 0
for comb in product(*all_path):
    ans = max(ans, total_sum(comb))
print(ans)
# print(total_sum())