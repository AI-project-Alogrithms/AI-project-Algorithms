# 이중 우선순위 큐 --> 다시 풀기
import heapq
import sys
sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
import heapq

T = int(input())
for _ in range(T):
    q = []
    k = int(input())
    for _ in range(k):
        s, num = input().rstrip().split()
        print("q: ", q)
        if s=='I': # 삽입
            heapq.heappush(q, int(num))
        elif q and s=='D': # 삭제
            if int(num)==1:
                q.pop()
            elif int(num)==-1:
                heapq.heappop(q)
    print(q)
    if len(q)==0:
        print("EMPTY")
    else:
        print(q[-1], end=" ")
        print(heapq.heappop(q))

