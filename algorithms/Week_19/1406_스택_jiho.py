# 에디터 
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import deque

# 커서 왼쪽 문자들/커서 오른쪽 문자들
# left_stack = deque()
right_stack = deque()

def add(x):
    # 왼쪽 커서에 문자열 추가
    left_stack.append(x)

def left():
    if left_stack:
        right_stack.appendleft(left_stack.pop())

def right():
    if right_stack:
        left_stack.append(right_stack.popleft())

def delete():
    if left_stack:
        left_stack.pop()


left_stack = deque(list(input().rstrip())) # 처음에 커서가 맨 오른쪽에 있음

N = int(input())

for _ in range(N):
    lst = list(input().rstrip().split())
    if lst[0]=='P':
        add(lst[1])
        # print(stack, cur)
    elif lst[0]=='L':
        left()
    elif lst[0]=='D':
        right()
    else:
        delete()

print("".join(map(str, left_stack))+"".join(map(str, right_stack)))