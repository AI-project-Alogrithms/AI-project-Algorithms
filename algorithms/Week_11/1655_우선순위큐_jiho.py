# 가운데를 말해요
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
import heapq


N= int(input())
leftheap = []
rightheap = []

for _ in range(N):
    num = int(input())
    if len(leftheap) == len(rightheap): # 둘중에 leftheap먼저 넣기
        heapq.heappush(leftheap, -num) # 최대 힙
    else:
        heapq.heappush(rightheap, num) # 최소 힙

    if rightheap and rightheap[0] < -leftheap[0]: # rightheap이 존재하고, rightheap의 가장 작은 값이 leftheap의 가장 큰 값보다 작다면 둘이 교체하기
        leftval = heapq.heappop(leftheap)
        rightval = heapq.heappop(rightheap)
        heapq.heappush(leftheap, -rightval)
        heapq.heappush(rightheap, -leftval)
    print(-leftheap[0])

