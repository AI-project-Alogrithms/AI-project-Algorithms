# 효도 음식 --> O(N) 시간 복잡도가 나오도록 하는게 중ㅇ함
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def comb_max(arr):
    max_ending_here = max_so_far = arr[0]
    max_sum = [0]*len(arr)
    max_sum[0] = arr[0]
    for i in range(1,len(arr)):
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)
        max_sum[i] = max_so_far
    return max_sum

def solve():
    global max_v
    # 각 위치에서 왼쪽 부분 배열 최대 합 계산
    left_max_sums = comb_max(arr)

    # 오른쪽 부분 배열의 합 계산 -> 배열 뒤집어서 처리
    right_max_sum = comb_max(arr[::-1])
    right_max_sum = right_max_sum[::-1] # 다시 뒤집어주기

    for cur in range(1,N-1):
        # # if cur ==0:continue
        # left = arr[:cur]
        # right = arr[cur+1:]
        # max_left = comb_max(left)
        # max_right = comb_max(right)
        max_v = max(max_v, left_max_sums[cur-1]+right_max_sum[cur+1])
    print(max_v)

N = int(input())
arr = list(map(int, input().split()))
max_v = -1000*100001
solve()

