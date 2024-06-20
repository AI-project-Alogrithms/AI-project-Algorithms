# 사다리 조작
import sys
from sys import stdin
sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

# 세로선 개수 n, 가로선 개수 m, 세로선마다 가로선을 놓을 수 있는 위치 개수 h
#  (2 ≤ N ≤ 10, 1 ≤ H ≤ 30, 0 ≤ M ≤ (N-1)×H)
n,m,h = map(int, input().split())
arr = []
for _ in range(m):
    a, b = map(int, input().split())
    arr.append([a,b])
print(arr)
# 사다리입력, 후보좌표 저장 pos = [] -> 3개 선택
# cnt개 중 0,1,2,3 => 조합 진행
