# 연탄의 크기
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
# from itertools import product

n = int(input())
home = list(map(int, input().split()))

r = 2
max_c, cnt = 0,0
while(r <= max(home)):
    for h in home:
        if h%r==0:
            cnt+=1
    max_c = max(max_c, cnt)
    cnt = 0
    r +=1
print(max_c)
