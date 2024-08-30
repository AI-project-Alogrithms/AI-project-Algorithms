# 트리
import sys
sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def dfs(num, arr):
    print(arr[num])
    arr[num] = -2
    for i in range(len(arr)):
        if num == arr[i]: # 삭제할 노드를 부모노드로 가지고 있는 애들도 삭제
            dfs(i, arr)

n = int(input())
arr = list(map(int, input().split()))
k = int(input())
count = 0
print(arr)
dfs(k, arr)
count = 0
for i in range(len(arr)):
    if arr[i] != -2 and i not in arr: # 삭제할 노드 중에서 부모노드로 가지고 있지 않는 노드 찾기
        count += 1
print(count)
