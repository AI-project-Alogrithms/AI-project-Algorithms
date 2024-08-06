# 주행시험장 ?? 모르겠음
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline


def binary_search(n, m):
    start, end = 1, max(n, m)
    min_dist = float('inf')
    k = end

    while start <= end:
        mid = (start + end) // 2
        dist = (n + mid - 1) // mid + (m + mid - 1) // mid
        if dist < min_dist:
            min_dist = dist
            k = mid
        if (n + mid - 1) // mid > (m + mid - 1) // mid:
            start = mid + 1
        else:
            end = mid - 1

    return k, min_dist



T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    k, min_dist = binary_search(n,m)
    print(k, min_dist)