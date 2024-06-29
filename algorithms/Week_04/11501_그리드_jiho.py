# 주식
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

T = int(input())
for _ in range(T): # 테스트 케이스
    n = int(input())
    lst = list(map(int, input().split()))
    # print(lst)
    ans = 0
    lst.reverse()
    max_v = lst[0] # 주가가 내릴 때 차액 계산
    for i in range(len(lst)):
        if lst[i] > max_v:
            max_v = lst[i]
        else:
            ans += (max_v-lst[i])
    print(ans)


