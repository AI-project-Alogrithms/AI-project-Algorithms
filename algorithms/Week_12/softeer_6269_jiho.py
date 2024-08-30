# 비밀 메뉴
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

M,N,K = map(int, input().split())
mlst = list(map(int, input().split()))
nlst = list(map(int, input().split()))
ans = ""
if N<M:
    ans = "normal"
else:
    for i in range(N-M+1):
        # tmp = nlst[i:i+M]
        if mlst == nlst[i:i+M]:
            # print(mlst, nlst[i:i+M])
            ans = "secret"
            break
        else:
            ans = "normal"

print(ans)