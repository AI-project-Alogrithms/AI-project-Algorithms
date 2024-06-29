import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

# n = int(input())
stack = []
for i in range(int(input())):
    s = int(input())
    if s == 0:
        stack.pop()
    else:
        stack.append(s)
print(sum(stack))
