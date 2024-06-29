# 나무수확 level3
import sys
from sys import stdin
sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline


N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
max_v = 0
# 배열
arr = [[0]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    arr[i][1:] = list(map(int, input().split()))

did = [[0]*(N+1) for _ in range(N+1)]
yet = [[0]*(N+1) for _ in range(N+1)]

did[1][1] = arr[0][0] * 2 # 스프링 쿨러 설치한 경우 최대값
yet[1][1] = arr[0][0] # 스프링 쿨러 설치하지 않은 경우 최대값

def solution():
    for i in range(1,N+1):
        for j in range(1, N+1):
            yet[i][j] = max(yet[i-1][j], yet[i][j-1]) + arr[i][j] # 스프링 쿨러를 설치하지 않았을 때의 max값
            did[i][j] = max(max(did[i][j-1], did[i-1][j])+arr[i][j], max(yet[i-1][j],yet[i][j-1])+arr[i][j]*2)
            # 스프링 쿨러를 설치했을 때의 max값에 현재 위치를 더한것과, 스프링 쿨러를 설치하지 않았을 때의 max값에 현재 위치가 스프링 쿨러일때를 비교

    print(did[N][N])

solution()
