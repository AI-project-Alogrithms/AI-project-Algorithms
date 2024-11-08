# 최대 힙
import heapq
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

N = int(input())
q = []
for _ in range(N):
    x = int(input())
    if x==0:
        if len(q)==0:
            print(0)
        else:
            print(-heapq.heappop(q))
    else:
        heapq.heappush(q, -x)
