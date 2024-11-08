# 움직이는 미로 탈출
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

# def move(roof): # 벽 이동
#     for i in range(len(roof)):
#         roof[i] = [roof[i][0]+1, roof[i][1]]
#     return roof

def bfs(i,j):
    q = deque()
    q.append((i,j))
    cnt = 0 # 9 초동안 살아 남으면 됨 --> 이게 핵심이네
    while q:
        for _ in range(len(q)):
            # print("cnt: ", cnt)
            ci, cj = q.popleft()
            if [ci,cj] in roof: continue # 벽이라면 가지 않기
            if ci==0 or cnt == 9:
                print(1)
                return 1
            # v[ci][cj] = 0
            for d in range(9):
                ni, nj = ci+di[d], cj+dj[d]
                if 0<=ni<8 and 0<=nj<8:
                    if [ni,nj] not in roof:
                        q.append((ni,nj))
        # print("1초",roof, q)
        for i in range(len(roof)):
            roof[i] = [roof[i][0] + 1, roof[i][1]] # 벽 움직임
        cnt +=1

    print(0)

di = [0,-1,-1,-1,0,0,1,1,1]
dj = [0,-1,0,1,1,-1,1,0,-1]

arr = [list(input().rstrip()) for _ in range(8)]
v = [[0]*8 for _ in range(8)] # 방문 여부

roof = [] # 벽 좌표
for i in range(8):
    for j in range(8):
        if arr[i][j]=='#':
            roof.append([i,j])
if not roof:
    print(1)
else: # 벽이 있다면
    bfs(7,0) # 왼쪽 하단에서 시작

