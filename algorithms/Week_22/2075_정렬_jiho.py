import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
import heapq

n = int(input())
q = []
for _ in range(n):
    for elem in list(map(int, input().split())):
        if len(q)<n:
            heapq.heappush(q, elem) # 큐 길이가 n보다 작으면 다음 꺼 넣기
        else:
            if elem >q[0]: # q의 [0]보다 해당 요소가 크다면
                heapq.heappop(q) # 가장 작은 값 제거
                heapq.heappush(q, elem) # 해당 요소 추가

print(q[0])


