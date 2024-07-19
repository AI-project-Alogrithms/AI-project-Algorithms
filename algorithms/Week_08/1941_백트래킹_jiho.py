# 소문난 칠공주
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque
"""
** 처음에 당연히 dfs로 탐색함. 하지만 이렇게 하면 인접한 애들끼리만 뭉치기가 어려움 => bfs로 해야됨
DFS 탐색으로 십자 모양 갈라지는 탐색은 하기 어렵다.
- 경우의 수를 다 넣고, 이때, 7명 이상이면 의미 없음, bfs이용해서 다 연결되어있는지 확인
    - 두문제로 나눠서 짜보기
        1. 가능한 모든 경우
        2. 인접한 거 개수 체크
"""
def bfs(i,j):
    # 4방향, 범윈 내, 미방문, visited[ni][nj] == 1, v[ni][nj]==0
    v = [[0]*5 for _ in range(5)]
    q = deque([(i,j)])
    v[i][j] = 1
    cnt = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<5 and 0<=nj<5 and visited[ni][nj]==1 and v[ni][nj] == 0:
                v[ni][nj] =1
                cnt +=1
                q.append((ni,nj))

    return cnt == 7

def check(): # visited 배열에 필요한 사람이 표시가 되어있음
    for i in range(5):
        for j in range(5):
            if visited[i][j] == 1:
                return bfs(i,j)

def dfs(n, cnt, scnt): # 가능한 모든 경우의 수 돌리기
    global ans
    if cnt > 7: # 가지치기 - 이미 7명을 넘었으면 7공주 불가
        return

    if n==25:
        if cnt == 7 and scnt >= 4: # 7명 그룹이고, 4명 이상이 s인 경우
            if check(): # 실제 인접했는지 체크-> 모두 인접했으면 +1
                ans +=1
        return
    visited[n//5][n%5] = 1 # 해당 인덱스를 포함하는 경우
    dfs(n+1, cnt+1, scnt+int(arr[n//5][n%5]=='S')) # 포함하는 경우 => 1 더하기
    visited[n//5][n%5] = 0
    dfs(n+1, cnt, scnt) # 포함하지 않은 경우



arr = [list(map(str, input().rstrip())) for _ in range(5)]
ans = 0
visited = [[0]*5 for _ in range(5)]
# 핵생 번호 0~24, 포함 학생수, 다솜파 학생수
dfs(0,0,0)
print(ans)

