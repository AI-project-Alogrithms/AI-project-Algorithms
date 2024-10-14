import sys

# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

ans = [-1] * N  # 기본값은 모두 -1로 설정
stack = []

for i in range(N):
    # 스택이 비어 있지 않고, 현재 숫자가 스택의 top이 가리키는 인덱스의 숫자보다 크면
    while stack and lst[stack[-1]] < lst[i]:
        ans[stack.pop()] = lst[i]

    # 현재 인덱스를 스택에 추가
    stack.append(i)

print(" ".join(map(str, ans)))
