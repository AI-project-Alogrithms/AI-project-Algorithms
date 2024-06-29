# 스택수열
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
n = int(input())
stack = [1]
ans = []
dp = ['+'] # +, - 저장
for _ in range(n):
    ans.append(int(input())) # 수열
# print(ans)
# for i in range(2, n+1):
i = 2
while(True):
    if len(ans) == 0:
        print("\n".join(map(str, dp)))
        break
    if len(stack)!=0:
        if stack[-1] > ans[0]:
            print("NO")
            break
    if len(stack)!=0 and stack[-1] == ans[0]:
        stack.pop()
        ans.pop(0)
        dp.append('-')
    else:
        stack.append(i)
        dp.append('+')
        i +=1
    # print(stack)
    # print(dp)
    # print(ans)

