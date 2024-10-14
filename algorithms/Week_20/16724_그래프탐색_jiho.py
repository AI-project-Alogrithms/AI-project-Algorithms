# 피리 부는 사나이 => 사이클
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def dfs(ci, cj):
    global cnt
    # 방문 표시
    visited[ci][cj] = True
    cycle.append((ci,cj))

    # 현재 위치의 이동 방향
    if arr[ci][cj]=='U' and ci >0:
        ci-=1
    elif arr[ci][cj]=='D' and ci<N-1:
        ci+=1
    elif arr[ci][cj]=='L' and cj>0:
        cj-=1
    elif arr[ci][cj]=='R' and cj<M-1:
        cj+=1

    if visited[ci][cj]: # 이미 방문한 좌표인데, 해당 사이클 안에 있다면
        if (ci,cj) in cycle:
            cnt+=1
    else:
        dfs(ci,cj)

N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]

# 방문 표시
visited = [[False]*M for _ in range(N)]

# DFS 돌리기
cnt=0 # safe zone 개수
for i in range(N):
    for j in range(M):
        if not visited[i][j]:# 방문 전이면
            cycle = [] # 현재 위치에서 시작하는 사이클 만들기
            dfs(i,j)

print(cnt)
