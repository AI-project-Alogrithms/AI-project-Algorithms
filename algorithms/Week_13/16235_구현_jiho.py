import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def spring_summer():
    for i in range(N):
        for j in range(N):
            cnt = len(trees[i][j]) # 현재 위치 나무 개수
            for k in range(cnt):
                # 나무가 죽은 경우, 나이순이니까 그 뒤 나무들도 다 죽은거
                if arr[i][j] < trees[i][j][k]: # 나이만큼 양분이 존재하지 않는다면
                    # 죽은 나무 저장
                    for _ in range(k, cnt):
                        dead_trees[i][j].append(trees[i][j].pop()) # 트리에서 제거 동시에 (뒤에서부터 pop)
                    break
                else: # 나무가 성장
                    arr[i][j] -= trees[i][j][k]
                    trees[i][j][k]+=1

    # 죽은 나무들 양분 저장
    for i in range(N):
        for j in range(N):
            while dead_trees[i][j]:
                arr[i][j] += dead_trees[i][j].pop()//2


def fall_winter():
    for i in range(N):
        for j in range(N):
            # 현재 위치의 나무들 탐색
            for k in range(len(trees[i][j])):
                # 현재 나무 나이가 씨를 뿌릴 수 있는 상태
                if trees[i][j][k]%5==0:
                    for di, dj in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
                        ni, nj = i + di, j + dj
                        # 범위 체크
                        if ni < 0 or ni >= N or nj < 0 or nj >= N:
                            continue
                        # 새로 태어난 나무들 앞으로 삽입
                        trees[ni][nj].appendleft(1)
            # 밭에 양분 추가 (겨울)
            arr[i][j] += sd[i][j]

N, M, K = map(int, input().split()) # N행열, M개의 나무, K년 후
arr = [[5]*N for _ in range(N)] # 처음 양분 초기화
sd = [list(map(int, input().split())) for _ in range(N)] # 겨울애 SD로봇이 양분 추가할 거
trees = [[deque() for _ in range(N)] for _ in range(N)] # 나무들 상태 저장할 배열
dead_trees = [[list() for _ in range(N)] for _ in range(N)] # 위치별 죽은 나무들 저장할 배열

# M개의 나무 x,y,z
for _ in range(M):
    x,y,z = map(int, input().split())
    trees[x-1][y-1].append(z)

for _ in range(K):
    spring_summer() # 봄, 여름
    fall_winter() # 가을, 겨울
ans = 0
for i in range(N):
    for j in range(N):
        ans += len(trees[i][j]) # 남아있는 나무 개수 count
print(ans)
