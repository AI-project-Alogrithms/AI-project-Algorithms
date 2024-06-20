# 색종이 만들기
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def cut(r,c,n):
    current = arr[r][c]
    for i in range(r,r+n):
        for j in range(c,c+n):
            if current != arr[i][j]:
                half = n//2
                cut(r,c,half) # 1사
                cut(r,c+half, half) # 2사
                cut(r+half, c, half) # 3사
                cut(r+half, c+half, half) # 4사
                return
    color[current] +=1
    return

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
color = {0:0, 1:0} # 하얀: 0, 파랑: 1
cut(0,0,n)
print("\n".join(map(str, color.values())))