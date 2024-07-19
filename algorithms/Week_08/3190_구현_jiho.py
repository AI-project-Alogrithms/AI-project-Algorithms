# 뱀
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

def snake():
    dr = 0  # 회전 방향 현재 오른쪽, di.index(Di[dr]): 특정 값 인덱스 찾기
    hi, hj, ti, tj = 1,1,1,1 # 머리 좌표, 꼬리 좌표
    q = deque([(hi,hj)]) # 현재 뱀 위치 저장
    lenght = 1 # 뱀 길이
    c = 0 # 시간
    while(True):
        if len(lst) != 0:
            time, drr = lst[0] # 방향 회전 정보
            if c == time: # 해당 시간이 됐다면
                if drr == 'D': # 오른쪽 회전이라면
                    dr = D[dr]
                elif drr=='L': # 왼쪽 회전이라면
                    dr = L[dr]
                lst.pop(0)
        c += 1  # 시간 늘어남
        ni, nj = hi+di[dr], hj+dj[dr] # 다음 좌표 이동
        if arr[ni][nj] == -1 or (ni,nj) in q: break # 몸에 닿거나, 벽에 닿으면 종료
        if arr[ni][nj] == 1: # 사과를 만났으면
            arr[ni][nj] = 0 # 사과 먹기
            # arr[ni][nj] = 2 # 테스트
            q.append((ni,nj))
            lenght += 1  # 길이는 늘어남
        else: # 다음 좌표가 사과가 아니라면
            q.popleft() # 꼬리 줄어들기
            q.append((ni,nj))
            # arr[ni][nj] = 0 # 테스트
        hi, hj = ni, nj
    return c


N = int(input()) # 배열 N*N
K = int(input()) # 사과 개수
# 벽 -1로 둘러싸기
arr = [[-1]*(N+2)] + [[-1]+[0]*N+[-1] for _ in range(N)] + [[-1]*(N+2)]

# 좌표 index 맞추기, 사과 1
for _ in range(K):
    x, y = map(int, input().split())
    arr[x][y] = 1
# 변환 횟수 # [(3, 'D'), (15, 'L'), (17, 'D')]
lst = []
R = int(input())
for _ in range(R):
    time, drr = map(str, input().rstrip().split())
    lst.append((int(time), drr))

# 회전 오른쪽, 아래, 왼쪽, 위
    # 0,1,2,3
di = [0,1,0,-1]
dj = [1,0,-1,0]
D = [1,2,3,0]
L = [3,0,1,2]

c = snake()
print(c)





