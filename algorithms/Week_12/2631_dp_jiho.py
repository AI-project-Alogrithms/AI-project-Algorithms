# 줄세우기
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def binary_search(lst, target):
    start, end = 0, len(lst)-1
    while start<=end:
        mid = (start+end)//2
        if lst[mid] < target:
            start = mid+1
        else:
            end = mid-1
    return start

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

lst = [arr[0]] # 맨 처음 배열값 저장
for i in range(n):
    if lst[-1] < arr[i]:
        lst.append(arr[i])
    else:
        index = binary_search(lst, arr[i]) # 작다면 들어갈 인덱스 찾기
        lst[index] = arr[i] # 대체
    # print(lst)
print(n-len(lst))
# print(lst)