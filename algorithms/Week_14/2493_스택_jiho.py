# 탑
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
stack = [] # 현재 탑보다 높은 탑 인덱스 저장
ans = [0]*N

for i in range(N):
    # print("i", i)
    while stack and lst[stack[-1]] < lst[i]:
        # print("lst[stack[-1]] < lst[i]: ", lst[stack[-1]] < lst[i])
        stack.pop() # 제거

    if stack:
        ans[i] = stack[-1]+1
    stack.append(i)
    # print("stack: ", stack)
print(" ".join(map(str, ans)))