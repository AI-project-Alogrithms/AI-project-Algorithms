# 로또 --> 사전순 정렬을 안했는데 왜 자동으로 된지는 모르겠음
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

def roto(n,ans, start):
    if n==6:
        print(" ".join(map(str, ans)))
        return
    for i in range(start, k): # 이전에 선택한 요소 이후부터 선택하기
        roto(n+1, ans + [s[i]], i+1)

while(True):
    k_s = list(map(int, input().split()))
    # print(k_s)
    if k_s==[0]:
        break
    k = k_s[0]
    s = k_s[1:]
    s.sort()
    # print(s)
    roto(0, [], 0)
    print()