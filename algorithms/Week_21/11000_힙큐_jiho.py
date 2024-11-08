# 강의실 배정
import heapq
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
import heapq


N = int(input())
lst = []
for _ in range(N):
    s, t = map(int, input().split())
    lst.append((s,t))
lst.sort() # 시작 순 정렬
# print(lst)
# 가장 빨리 끝나는 시간 관리
q = []
heapq.heappush(q, lst[0][1]) # 첫번째 강의 넣기
# print(q)
# # # 나머지 강의 처리
for i in range(1, N):
    # 가장 빨리 끝나는 강의실의 끝나는 시간이 현재 강의 시작 시간보다 작거나 같으면 같은 강의실 사용
    if q[0] <= lst[i][0]:
        heapq.heappop(q)
    heapq.heappush(q, lst[i][1]) # 새로운 강의를 넣음
print(len(q))

