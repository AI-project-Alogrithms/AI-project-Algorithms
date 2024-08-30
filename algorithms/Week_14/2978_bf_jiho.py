# 블랙잭
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))
ans = 0
for i in range(N):
    for j in range(N):
        for k in range(N):
            if i==j or i==k or j==k or i==j==k: continue
            tmp = sum([lst[i],lst[j],lst[k]])
            if 0<= M-tmp<=M:
                ans = max(ans, tmp)
print(ans)

