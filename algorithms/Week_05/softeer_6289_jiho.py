# 우물안개구리 level 3
import sys
from sys import stdin
sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import defaultdict

n,m = map(int, input().split())

w = list(map(int, input().split()))
w = [0] + w

peo = {idx+1: [] for idx in range(n)}
# print(peo)
for _ in range(m):
    p1, p2 = map(int, input().split())
    peo[p1].append(p2)
    peo[p2].append(p1)
# print(peo)
cnt = 0
for key, value in peo.items():
    if len(value) == 0: # 혼자면
        cnt+=1
    else: # 비교할 사람이 있으면
        kw = w[key]
        vw = []
        for va in value:
            vw.append(w[va])
        if kw > max(vw):
            cnt +=1
print(cnt)




