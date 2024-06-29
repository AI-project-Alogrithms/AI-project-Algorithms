# 균형잡힌 세상
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

while(True):
    s = input().rstrip()
    if s == '.':
        break
    stack = []
    for i in s:
        if i == '(' or i == '[': # 시작 부분 이라면
            stack.append(i)
        elif i==')': # 닫힌 소괄호가 나왔다면
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop() # 제거
            else:
                stack.append(')')
                break
        elif i==']': # 닫힌 대활호가 나왔다면
            if len(stack)!=0 and stack[-1] == '[':
                stack.pop() # 제거
            else:
                stack.append(']')
                break
    if len(stack) == 0:
        print('yes')
    else:
        print('no')

    # print(s)