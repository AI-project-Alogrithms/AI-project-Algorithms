# N-Queen: 아이디어 - 룩업테이블
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def dfs(n):
    global cnt
    if n==N:
        cnt +=1
        return
    for j in range(N):
        if (v1[j]==v2[n+j]==v3[n-j]==0): # 열/대각선에 없는 경우
            v1[j] = v2[n + j] = v3[n - j] = 1
            dfs(n+1)
            v1[j] = v2[n + j] = v3[n - j] = 0

N = int(input())
cnt = 0
v1 = [0]*N
v2 = [0]*2*(N)
v3 = [0]*2*(N)
dfs(0)
print(cnt)