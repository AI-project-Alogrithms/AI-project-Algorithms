# 내려가기
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque
## 이전 값들만 저장하면 됨! ==> 슬라이싱 윈도우 이용하기 (DP를 꼭 다 담을 생각하지 않아도 됨)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

prev_max = arr[0]
prev_min = arr[0]

for i in range(1, n):
    cur_max = [0] * 3
    cur_min = [0] * 3

    cur_max[0] = max(prev_max[0], prev_max[1]) + arr[i][0]
    cur_min[0] = min(prev_min[0], prev_min[1]) + arr[i][0]

    cur_max[1] = max(prev_max[0], prev_max[1], prev_max[2]) + arr[i][1]
    cur_min[1] = min(prev_min[0], prev_min[1], prev_min[2]) + arr[i][1]

    cur_max[2] = max(prev_max[1], prev_max[2]) + arr[i][2]
    cur_min[2] = min(prev_min[1], prev_min[2]) + arr[i][2]

    prev_max = cur_max
    prev_min = cur_min

max_value = max(prev_max)
min_value = min(prev_min)
print(max_value, min_value)