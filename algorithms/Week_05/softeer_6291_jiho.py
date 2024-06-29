# 강의실 배정
import sys
import heapq
from sys import stdin
sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

time = []
cnt = 0
n = int(input())
for i in range(n):
    a,b = map(int, input().split())
    heapq.heappush(time,(b,a)) # # 가장 빨리 끝난느 수업을 기준으로 정렬

# 최소 힙을 사용하여 강의실 배정
cnt = 0
e = 0 # 시작시간

while time:
    print(time)
    b, a = heapq.heappop(time)
    print(b,a)
    if e <= a: #시작시간이 더 크면
        cnt += 1
        e = b # 시작시간을 종료시간으로 변환
print(cnt)
