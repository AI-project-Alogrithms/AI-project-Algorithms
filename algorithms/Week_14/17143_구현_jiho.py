# 낙시왕
import sys
sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
# 1,2,3,4 상, 하, 좌, 우
di = [0, -1, 1, 0, 0]
dj = [0, 0, 0,-1, 1]

def move():
    new_arr = [[[] for _ in range(C + 1)] for _ in range(R + 1)]
    for ci in range(1,R+1):
        for cj in range(1,C+1):
            if arr[ci][cj]: # 상어가 있다면
                s, d, z = arr[ci][cj].pop()
                si, sj = ci, cj
                # 상어 이동 해야할 실제 거리 계산 -> 주기 계산
                if d==1 or d==2: # 상하 이동이라면
                    s %= (R-1)*2 # 왕복 제자리로 오는 거리 계산
                else: # 좌우 이동 이라면
                    s %= (C-1)*2

                for _ in range(s):
                    ni, nj = si + di[d], sj + dj[d]
                    if ni <= 0 or ni > R or nj <= 0 or nj > C:
                        if d == 1: d = 2
                        elif d == 2: d = 1
                        elif d == 3: d = 4
                        else: d = 3
                        ni, nj = si + di[d], sj + dj[d]
                    si, sj = ni, nj

                if new_arr[si][sj]: # 새로운 위치에 상어 추가 이미 있다면
                    if new_arr[si][sj][0][2] < z:
                        new_arr[si][sj] = [(s, d, z)]
                else:
                    new_arr[si][sj].append((s, d, z))
    return new_arr


R, C, M = map(int, input().split())
arr = [[[] for _ in range(C+1)] for _ in range(R+1)] #낙시터

for _ in range(M): # 상어 정보
    r,c,s,d,z = map(int, input().split())
    arr[r][c].append((s,d,z)) # 상어 표시

# 낙시왕 이동
ans = 0
for j in range(1,C+1):
    for i in range(1, R+1):
        if arr[i][j]: # 한마리 잡기
            s, d, z = arr[i][j].pop()
            ans += z
            break
        # 상어 이동
        arr = move()
print(ans)
# for i in arr:
#     print(i)