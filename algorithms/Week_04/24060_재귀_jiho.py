# 알고리즘 - 병합정렬: 모르겠음...하
import sys
from sys import stdin
sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def merge(left, right, cnt):
    i, j = 0,0
    sorted_list = []
    global answer
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            if cnt == th:
                answer = left[i]
            i += 1
            cnt += 1

        else:
            sorted_list.append((right[j]))
            if cnt == th:
                answer = right[j]
            j+=1
            cnt += 1
    while i < len(left):
        sorted_list.append(left[i])
        if cnt == th:
            answer = left[i]
        i += 1
        cnt += 1
    while j < len(right):
        sorted_list.append(right[j])
        if cnt == th:
            answer = right[j]
        j += 1
        cnt += 1
    return sorted_list, cnt

def merge_sort(arr, cnt):
    # 길이가 1이 될때까지 쪼개기
    if len(arr) <=1:
        return arr
    # 리스트 분할
    mid = len(arr)//2 # 3 3
    left = arr[:mid]
    right = arr[mid:]

    # 분할된 리스트 각각 merge sort 진행
    left_m= merge_sort(left, cnt)
    right_m = merge_sort(right, cnt)

    return merge(left_m, right_m, cnt)

n, th = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
print(merge_sort(arr, 0))
print(answer)

