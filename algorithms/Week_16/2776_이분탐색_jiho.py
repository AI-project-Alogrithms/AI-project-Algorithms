# 암기왕
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def binary_search(num):
    start, end = 0, N-1
    ans = 0
    while(start<=end):
        mid = (start+end)//2
        # print(num, mid, olst[mid])
        if num == olst[mid]:
            ans = 1
            break
        elif num < olst[mid]:
            end = mid-1
        elif num > olst[mid]:
            start = mid+1
    return ans

T = int(input())
for _ in range(T):
    N = int(input())
    olst = list(map(int, input().split()))
    olst.sort()
    # print(olst)
    M = int(input())
    tlst = list(map(int, input().split()))
    # print(tlst)
    for i in tlst:
        print(binary_search(i))