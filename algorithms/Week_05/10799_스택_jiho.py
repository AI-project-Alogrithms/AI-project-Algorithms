# import sys
# from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
# input = sys.stdin.readline

arr = list(input())
# print(arr)

# 어떻게 count해야되는지 고민을 많이 하다 결국 해설봄
cnt = 0
stack = []
for i in range(len(arr)):
    if arr[i] == '(': # 인풋
        stack.append(i)
    else: #")" 일때
        if arr[i-1] == "(": # 레이저라면
            stack.pop()
            cnt +=len(stack)
        else: # ) 라면, 그냥 혼자 끝내는거
            stack.pop()
            cnt += 1
print(cnt)


# print(new_arr)



