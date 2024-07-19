# 스타트택시
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

def bfs(ti, tj): # 전체 돌면서 최단거리 바로 구하기
    q = deque([(ti, tj)])
    arr_copy = [[-1]*(N+2) for _ in range(N+2)] # 배열 복제, -1로 초기화 (방문 안한곳 표시)
    arr_copy[ti][tj] = 0  # 시작점 방문 표시
    while(q):
        ci, cj = q.popleft()
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci+di, cj+dj
            if arr[ni][nj] != 1 and arr_copy[ni][nj] == -1: # 방문전이고, 장애물이 아니면
                arr_copy[ni][nj] = arr_copy[ci][cj] +1
                q.append((ni, nj))
    # for i in arr_copy:
    #     print(i)
    return arr_copy # 목적지에 도달하지 못하면 -1 반환

def get_distance(ti, tj, target_i, target_j):
    distance = bfs(ti, tj)
    return distance[target_i][target_j]

N, M, engine = map(int, input().split())
arr = [[1]*(N+2)]+[[1]+list(map(int, input().split()))+[1] for _ in range(N)] + [[1]*(N+2)]
# for i in arr:
#     print(i)
ti, tj = map(int, input().split()) # 택시 초기 위치
ans = engine
plst = []
for _ in range(M):
    pi, pj, fi, fj = map(int, input().split())
    plst.append([pi, pj, fi, fj])  # 승객 정보 저장

while (len(plst)!=0):
    distances  = bfs(ti, tj) # 모든 좌표에서의 최소 거리 반환
    # M명의 승객,
    for people in plst:
        people.append(distances [people[0]][people[1]]) # 최단거리 함께 저장
    # print(plst)
    # 저장된 최단거리 중 가장 짧은 거, 핼, 열 가장 작은 사람 순으로 이동 => 인덱스 잘보자!!
    plst.sort(key=lambda x: (x[4],x[0],x[1]))
    # print(plst)

    # for people in plst:
    pi, pj, fi, fj, d = plst.pop(0)
    if d == -1 or engine < d: # 가는길에 엔진이 다 떨어지면, 갈수 없는 곳이면
        ans = -1
        break

    engine -= d  # 사람 위치로 택시 이동
    ti, tj = pi, pj  # 사람 위치로 택시 이동
    distance_to_engine = get_distance(ti, tj, fi, fj)
    if distance_to_engine == -1 or engine < distance_to_engine:
        ans = -1
        break

    engine+= distance_to_engine # 엔진 채우기
    ti, tj = fi, fj # 현재 위치 목적지 위치로 이동
    for people in plst:
        people.pop() # 최단 거리 제거

if ans != -1:
    print(engine)
else:
    print(ans)





