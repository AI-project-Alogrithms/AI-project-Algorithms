# 진정한 효도 level2
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(3)]
t_arr = list(map(list, zip(*arr)))

arr = arr+t_arr
# print(arr)
total_v = []
for i in range(6):
    nlist = set(arr[i])
    # print(nlist)
    if len(nlist) == 1:
        tmp = 0
    elif len(nlist) == 2:
        tmp = abs(list(nlist)[0] - list(nlist)[1])
    else:
        tmp = 2
    total_v.append(tmp)
print(min(total_v))
