# 미세먼지 안녕!: bfs, lotation
"""
visited 방문은 한번만 도는거니까 필요 없어서 제외, 그리고 5보다 작은건 굳이 spread할 필요 없으니 미리 넣어주기
"""
import sys
# from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

def bfs(arr,qr): # 미세먼지 확산
    q = deque(qr)
    arr_co = [[0]*C for _ in range(R)]
    while(q):
        ci, cj = q.popleft() # 현재 미세먼지 pop
        if arr[ci][cj] < 5: # 5보다 작으면 안퍼짐
            arr_co[ci][cj] += arr[ci][cj] # 그냥 넣기
            continue
        spread = arr[ci][cj]//5 # 5 보다 크면 퍼트리기
        cnt = 0 # 몇개 위치 퍼지는지
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<R and 0<=nj<C and (ni, nj) not in air_location:
                # 범위내, 현재 위치에서 미방문, 공기 청정기 위치가 아니면
                arr_co[ni][nj] += spread
                cnt +=1
        arr_co[ci][cj] = arr[ci][cj]-(spread*cnt) + arr_co[ci][cj] # copy에 저장된것도 더해주기
    # arr_b = [a[:] for a in arr_co] # 미세먼지 확산된 것으로 arr 바꾸기
    return arr_co


def rotate_air(arr):  # 공기 청정기 작동
    ai1, aj1 = air_location[0]
    ai2, aj2 = air_location[1]

    # 위쪽 공기청정기 (반시계 방향) ==> 미세먼지가 이동하는건 시계방향
    for i in range(ai1 - 1, 0, -1):
        arr[i][0] = arr[i - 1][0]
    for j in range(0, C - 1):
        arr[0][j] = arr[0][j + 1]
    for i in range(0, ai1):
        arr[i][C - 1] = arr[i + 1][C - 1]
    for j in range(C - 1, 1, -1):
        arr[ai1][j] = arr[ai1][j - 1]
    arr[ai1][1] = 0 # 처음 뻗어나가는 곳을 마지막에 0처리 해주면 복사 굳이 안해도 됨

    # 아래쪽 공기청정기 (시계 방향) => 미세먼지가 이동하는건 반시계 방향
    for i in range(ai2 + 1, R - 1):
        arr[i][0] = arr[i + 1][0]
    for j in range(0, C - 1):
        arr[R - 1][j] = arr[R - 1][j + 1]
    for i in range(R - 1, ai2, -1):
        arr[i][C - 1] = arr[i - 1][C - 1]
    for j in range(C - 1, 1, -1):
        arr[ai2][j] = arr[ai2][j - 1]
    arr[ai2][1] = 0

    return arr






R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
air_location = []
for i in range(R):
    for j in range(C):
        if arr[i][j] == -1:  # 공기 청정기 위치
            air_location.append((i, j))
# for i in arr:
#     print(i)
while(T>0):
    qr = [] # 동시에 확산 => 미리 큐에 담아두기
    for i in range(R):
        for j in range(C):
            if arr[i][j] != 0 and arr[i][j] != -1:  # 미세먼지 위치
                qr.append((i, j))
    arr = bfs(arr,qr) # 미세먼지 확산
    # print("확산 후 \n")
    # for i in arr:
    #     print(i)
    fi_arr = rotate_air(arr) # 공기 청정기 작동
    # print("작동 후 \n")
    # for i in fi_arr:
    #     print(i)
    T-=1 # 시간 줄어들기

# 남아있는 미세먼지 양 합치기
sum_arr = sum(fi_arr,[])
ans = sum(sum_arr)
print(ans)