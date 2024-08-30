# 마법사 상어와 비바라기
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def move(di, si):
    new_cloud = []
    # 방향, 칸개수
    for ci, cj in cloud:
        ni, nj = (ci+d[di][0]*si)%N, (cj+d[di][1]*si)%N
        new_cloud.append((ni,nj))
        v[ni][nj] = 1 # 구름 생긴 곳
    # for ci, cj in new_cloud:
    #     print(arr[ci][cj],end=" ")
    return new_cloud

def rain(new_cloud):
    for ci, cj in new_cloud:
        arr[ci][cj]+=1 # 비 내리기
    # new_cloud=[] # 구름 소멸
    # return new_cloud

def add(cloud):
    while cloud:
        ci, cj = cloud.pop(0) # 구름 소멸과 함께 물 채우기
        cnt = 0 # 대각선 물 있는 개수
        for i in range(2, 9, 2): # 대각선만
            ni, nj = ci+d[i][0], cj+d[i][1]
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] != 0: # 물이 들어있다면
                cnt +=1
        arr[ci][cj] += cnt
    return cloud

def make(cloud):
    # 구름 생성
    for i in range(N):
        for j in range(N):
            if v[i][j] != 1 and arr[i][j] >= 2: # 구름 생기는 조건
                cloud.append((i,j)) # 구름 생성
                arr[i][j] -=2 # 2 마이너스
    return cloud

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)] # 바구니 물의 양
location = [list(map(int, input().split())) for _ in range(M)] # 이동 정보
cloud = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)] # 처음 구름 좌표
d = [(0,0),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)] # 방향


while(len(location)!=0):
    di, si = location.pop(0) # 이동 정보
    v = [[0] * N for _ in range(N)]  # 구름 만들어진 곳

    # 구름 이동
    cloud = move(di, si)

    # 비 내리기, 구름 소멸
    rain(cloud)

    # 물 증가
    cloud = add(cloud)

    # 구름 생성, 물 -2
    cloud = make(cloud)

    # for i in arr:
    #     print(i)
    # for ci, cj in cloud:
    #     print(arr[ci][cj], end=" ")
    # print()
ans = sum(map(sum, zip(*arr)))
print(ans)
