#  sort, 차이 배열 이용해서 시간 초과 줄이기
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
# from collections import defaultdict

N, K = map(int, input().split())
lst = [0]*(N+1)

# print(dicts)
for _ in range(K):
    a, b = map(int, input().split())
    # a-1 번째 인덱스는 +1, b번째 인덱스는 -1
    lst[a-1] +=1
    if b<N:
        lst[b] -=1 # 다시 원래 값으로 돌리기!

# 누적합 계산해서 실제 배열로 변환
cum = 0
ans = []
for i in range(N):
    cum += lst[i]
    ans.append(cum)
# print(ans)
ans.sort()
print(ans[N//2])