# 절대값 힙
import heapq
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
import heapq
N = int(input())
left = []
right = []
for _ in range(N):
    x = int(input())
    if x==0:
        if len(left)==0 and len(right)==0:
            print(0)
        elif len(left)==0:
            print(heapq.heappop(right))
        elif len(right)==0:
            print(-heapq.heappop(left))
        else:
            if left[0]<=right[0]:
                print(-heapq.heappop(left))
            else:
                print(heapq.heappop(right))
    else:
        if x<0:
            heapq.heappush(left, abs(x))
        else:
            heapq.heappush(right, x)

