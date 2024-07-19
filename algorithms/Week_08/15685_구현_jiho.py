# 드래곤 커브
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

N = int(input())
arr = [[0]*101 for _ in range(101)]
di = [0,-1,0,1]
dj = [1,0,-1,0]

for _ in range(N):                               # 드래곤 커브 개수만큼 입력받기
    sj, si, dr, g = map(int, input().split()) # j,i순인거 잘 보기!!!
    lst = [(si, sj)] # 시작 위치
    lst.append((si+di[dr], sj+dj[dr]))           # 0 세대 위치 저장
    for _ in range(g):                           # 세대 횟수만큼 뻗어가기
        ei, ej = lst[-1] # lst의 끝 좌표 기준으로 90도 회전
        for i in range(len(lst)-2, -1, -1): # 1씩 빼주면서 전체 체크
            ci, cj = lst[i]
            lst.append((ei-(ej-cj), ej+(ei-ci)))
    # arr에 드레곤 커브 표시
    for i, j in lst:
        # if 0 <= i <= 100 and 0 <= j <= 100:
        arr[i][j] = 1

# 2*2 네 칸이 모두 1인 경우 찾기
ans = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == arr[i+1][j] == arr[i][j+1] == arr[i+1][j+1] == 1:
            ans +=1
print(ans)
