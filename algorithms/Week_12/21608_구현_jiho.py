# 상어 초등학교
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import defaultdict
N = int(input())
n = N*N
child_dict = defaultdict(list)
for _ in range(n):
    tmp = list(map(int, input().split()))
    child_dict[tmp[0]] = tmp[1:]
# print(child_dict)
clst = list(child_dict.keys())
arr = [[0]*N for _ in range(N)] # 자리배치
tlst = [-1]*(n+1) # 좌표 저장

# 자리배치 초기화: 첫번째 학생 배치 ==> 꼭 가운데가 첫번재 위치가 아닐 수도 있음
# arr[N//2][N//2] = clst[0]
# tlst[clst[0]] = (N//2, N//2)
# print(tlst)

# 학생들이 돌면서 자리배치
for i in range(n): #  3, 9, 8, 7, 1, 6, 5, 2]
    # 인접한 개수 구하기
    candi = []
    likelst = child_dict[clst[i]] # 좋아하는 숫자 리스트 [1, 9, 4, 5]
    # 모든 좌표 탐색
    for x in range(N):
        for y in range(N):
            if arr[x][y] == 0: # 빈자리만 확인
                like_cnt = 0 # 좋아하는 수
                empty_cnt = 0 # 비어있는 수

                # 상하좌우 탐색
                for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ni, nj = x + di, y + dj
                    if 0 <= ni < N and 0 <= nj < N:
                        if arr[ni][nj] in likelst: # 좋아하는 숫자라면
                            like_cnt +=1
                        if arr[ni][nj]==0:
                            empty_cnt+=1 # 해당 자리가 비어있다면
                candi.append((like_cnt,empty_cnt,x,y))
    # 좋아하는 수, 비어있는, 행, 열 sort
    candi.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    # print(candi)
    _, _, cdi, cdj = candi[0] # 배열에 추가,
    arr[cdi][cdj] = clst[i]
    tlst[clst[i]] = (cdi, cdj)
# for i in arr:
#     print(i)
# 모든 좌표 탐색
alst = [0,1,10,100,1000]
ans = 0
for x in range(N):
    for y in range(N):
        ta = arr[x][y]
        cnt = 0
        # 상하좌우 탐색
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = x + di, y + dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] in child_dict[ta]:
                cnt +=1
        ans += alst[cnt]
print(ans)




