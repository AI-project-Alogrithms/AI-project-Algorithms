# 문자열 폭발
import sys
from sys import stdin
sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

lst = input().rstrip()
bom = input().rstrip()
bom_len = len(bom)

stack = [] # 스택 사용
for i in range(len(lst)): # 문장의 길이만큼 돌아가는 동안
    stack.append(lst[i]) # 스택에 저장
    # print(stack)
    # print("".join(stack[-bom_len:]))
    if "".join(stack[-bom_len:]) == bom: # 폭발과 같을 때
        for j in range(bom_len):
            stack.pop()
            # print(stack)

if len(stack) == 0:
    print("FRULA")
else:
    print("".join(map(str, stack)))