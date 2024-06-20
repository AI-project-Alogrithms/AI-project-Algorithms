# 종이의 개수
import sys
from sys import stdin
sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def cut(r,c,n):
    current = arr[r][c] # 현재 값 저장
    for i in range(r, r+n):
        for j in range(c, c+n): # 9 -> 3-> 1
            if arr[i][j] != current: # 현재 종이 종류와 다르다면
                # 종이 분할
                half = n//3
                # 종이를 9등분하기
                cut(r,c,half)
                cut(r,c+half,half)
                cut(r,c+(half*2), half)
                cut(r+half, c, half)
                cut(r+half, c+half, half)
                cut(r+half, c+(half*2), half)
                cut(r+(half*2), c, half)
                cut(r+(half*2), c+half, half)
                cut(r+(half*2), c+(half*2), half)
                return
    cnt[current] +=1
    return

n = int(input())
# 배열 입력
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = {-1: 0, 0:0, 1:0}
cut(0, 0, n)
# print(cnt)
print("\n".join(map(str, cnt.values())))
