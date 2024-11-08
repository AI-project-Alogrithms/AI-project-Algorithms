# 보석 도둑
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
import heapq

N, K = map(int, input().split())
jew = [] # 보석
for _ in range(N): # 무게가 작은 것부터 나오게 하기
    heapq.heappush(jew, list(map(int, input().split())))
bags = []
for _ in range(K):
    bags.append(int(input()))
bags.sort() # 작은 순서대로 정렬
ans = 0
tmp_jew = []
for bag in bags:
    while jew and bag>=jew[0][0]: # 현재 가방 무게에 들어갈 수 있는 보석들 저장
        heapq.heappush(tmp_jew, -heapq.heappop(jew)[1])
        # print(jew)
        # print(tmp_jew)
    if tmp_jew:
        # tmp_jew가 있다면
        ans-=heapq.heappop(tmp_jew) # 최대 힙만 저장
        # print("ans: ", ans)
    elif not jew:
        break
print(ans)