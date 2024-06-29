import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

stack = []
for _ in range(int(input())):
    s = list(input().rstrip().split())
    # print(s)
    if len(s) > 1: # push
        stack.append(int(s[1]))
    if s[0]=='pop':
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)
    if s[0]=='size':
        print(len(stack))
    if s[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    if s[0] == 'top':
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)