# 카드 정렬하기
import heapq
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
import heapq

N = int(input())

q = []
for _ in range(N):
    heapq.heappush(q, int(input()))
ans = 0
if len(q) == 1:
    print(0)
else:
    while q:
        tmp = heapq.heappop(q)
        if q:
            tmp+= heapq.heappop(q)
        ans+=tmp
        if not q:
            break
        heapq.heappush(q, tmp)
    print(ans)
