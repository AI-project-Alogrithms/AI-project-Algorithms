# 2048
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def left(arr):
    for i in range(N):
        c = 0 # 현재 가리키는 곳 위치
        for j in range(N):
            if arr[i][j] !=0: # 0 이 아니면
                tmp = arr[i][j]
                arr[i][j] = 0
                if arr[i][c]==0:
                    arr[i][c] = tmp
                elif arr[i][c]==tmp:
                    arr[i][c] *=2
                    c+=1
                else: # 0도 아니고, 같지도 않다면
                    c+=1
                    arr[i][c] = tmp # 다음칸에 tmp넣기
    return arr

def right(arr):
    for i in range(N):
        c = N-1 # 현재 가리키는 곳 위치
        for j in range(N-1,-1,-1):
            if arr[i][j] !=0: # 0 이 아니면
                tmp = arr[i][j]
                arr[i][j] = 0
                if arr[i][c]==0:
                    arr[i][c] = tmp
                elif arr[i][c]==tmp:
                    arr[i][c] *=2
                    c-=1
                else: # 0도 아니고, 같지도 않다면
                    c-=1
                    arr[i][c] = tmp # 다음칸에 tmp넣기
    return arr

def up(arr):
    for j in range(N):
        c = 0 # 현재 가리키는 곳 위치
        for i in range(N):
            if arr[i][j] !=0: # 0 이 아니면
                tmp = arr[i][j]
                arr[i][j] = 0
                if arr[c][j]==0:
                    arr[c][j] = tmp
                elif arr[c][j]==tmp:
                    arr[c][j] *=2
                    c+=1
                else: # 0도 아니고, 같지도 않다면
                    c+=1
                    arr[c][j] = tmp # 다음칸에 tmp넣기
    return arr

def down(arr):
    for j in range(N):
        c = N-1 # 현재 가리키는 곳 위치 => 행
        for i in range(N-1,-1,-1):
            if arr[i][j] !=0: # 0 이 아니면
                tmp = arr[i][j]
                arr[i][j] = 0
                if arr[c][j]==0:
                    arr[c][j] = tmp
                elif arr[c][j]==tmp:
                    arr[c][j] *=2
                    c-=1
                else: # 0도 아니고, 같지도 않다면
                    c-=1
                    arr[c][j] = tmp # 다음칸에 tmp넣기
    return arr


def dfs(n, arr):
    global ans
    if n==5: # 5번 다 돌았다면 그때 arr의 max값 추출
        cnt = max(map(max, zip(*arr)))
        ans = max(ans, cnt)
        return
    for i in range(4):
        arr_copy = [a[:] for a in arr]
        if i==0:
            dfs(n+1, left(arr_copy))
        elif i==1:
            dfs(n+1, right(arr_copy))
        elif i==2:
            dfs(n+1, up(arr_copy))
        else:
            dfs(n+1, down(arr_copy))

N = int(input()) # 보드의 크기
arr = [list(map(int, input().split())) for _ in range(N)] # 게임판 초기 상태
ans = 0
# 이동: 최대 5번
dfs(0, arr)
print(ans)