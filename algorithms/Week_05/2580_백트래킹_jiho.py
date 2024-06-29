# 스도쿠
import sys
# sys.setrecursionlimit(5000)
from sys import stdin
sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
# from collections import deque

def isrow(x, n): # 가로
    for i in range(9): # 행을 돌동안
        if n == arr[x][i]:
            return False
    return True

def iscol(y, n): # 세로
    for i in range(9): # 행을 돌동안
        if n == arr[i][y]:
            return False
    return True

def box(x, y, n): # 박스
    for i in range(3):
        for j in range(3):
            if n == arr[x//3*3 + i][y//3*3+j]: # 칸 내에 이미 있으면
                return False
    return True


def find(n):
    if n==len(blank): # 빈곳만큼 사용했으면
        for i in arr:
            print(" ".join(map(str, i)))
        exit() # 강제 종료
    for i in range(1,10):
        ci, cj = blank[n][0], blank[n][1] # 빈곳 위치
        if isrow(ci, i) and iscol(cj, i) and box(ci, cj, i):
            # 모두 해당 i가 없으면
            arr[ci][cj] = i
            find(n+1)
            arr[ci][cj] = 0
        # 있는 경우는 생각할 필요 없음. 안넣는거임

arr = [list(map(int, input().split())) for _ in range(9)]
# print(arr)
# 빈 곳 위치 저장
blank = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            blank.append((i,j))
# print(blank)

find(0)




