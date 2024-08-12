# 톱니바퀴
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

lst = []
N = 4 # 일반화 시키기
arr = [[0]*8]+[list(map(int, input().rstrip())) for _ in range(N)]
k = int(input()) # 2번 회전
top = [0]*(N+1)

for _ in range(k): # K번 idx, dr
    idx, dr = map(int, input().split()) # 회전할 번호, 방향
    # [1] idx 톱니를 회전
    tlst = [(idx, 0)] # 같은 방향 (짝수 방향)
    # [2] idx 우측방향 처리(같은 극성 나오면 탈출)
    for i in range(idx+1, N+1):
        # 왼쪽 3 시 극성 != 오른쪽 9시 극성 => 회전후보 추가
        if arr[i-1][(top[i-1]+2)%8] != arr[i][(top[i]+6)%8]:
            tlst.append((i,(i-idx)%2))
        else: # 같은 극성이면 더이상 전달 안됨
            break
    # [3] idx 좌측방향 처리(같은 극성 나오면 탈출)
    for i in range(idx-1, 0, -1):
        # 왼쪽 3 시 극성 != 오른쪽 9시 극성 => 회전후보 추가
        if arr[i][(top[i]+2)%8] != arr[i+1][(top[i+1]+6)%8]:
            tlst.append((i,(idx-i)%2))
        else: # 같은 극성이면 더이상 전달 안됨
            break

    # [4] 실제 회전 처리(cw이면 top값을 -1)
    for i, rot in tlst:
        if rot == 0: # idx 톱니의 dr과 같은 방향
            top[i] = (top[i]-dr+8)%8
        else: # 다른 방향
            top[i] = (top[i]+dr+8)%8
# 점수를 계산
ans = 0
tables = [0,1,2,4,8]
for i in range(1, N+1):
    ans += arr[i][top[i]]*(tables[i])
print(ans)