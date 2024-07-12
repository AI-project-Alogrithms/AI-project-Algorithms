# 개똥벌레 => 이분탐색 연습용으로 제일 좋음 다시 풀기
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from collections import defaultdict

def binary_search(arr, x): # 현재 높이 x보다 데이터의 개수 반환
    left = 0 # 인덱스 0부터 시작
    right = len(arr)-1 # 맨끝 인덱스
    while(left<=right):
        mid = (left+right)//2
        if arr[mid] <= x:
            left = mid+1
        else:
            right = mid-1
    return len(arr) - (right+1) # index, 개수 차이로 +1

N, H = map(int, input().split())
arr_up = []
arr_down = []
for i in range(N):
    k = int(input())
    if i%2==0:
        arr_down.append(k)
    else:
        arr_up.append(k)
arr_up.sort()
arr_down.sort()
ans = N # 장애문의 최소값 => N개의 장애물 다 걸렸을 때
cnt = 0 # 구간 개수
for h in range(1,H+1): # 높이 만큼 돌동안 (최대 높이 만큼 올라갈동안)
    down_n = binary_search(arr_down, h-1) # 높이 0부터 시작해서 h까지 올라가기
    up_n = binary_search(arr_up, H-h) # 최대 높이 부터 시작해서 내려가기
    cur_num = down_n + up_n # 현재 mid값을 기준으로 잘랐을 때 장애물의 수
    if cur_num < ans: # 새로운 최소값이 나오면 업데이트
        ans = cur_num
        cnt = 1 # 개수 초기화 => 새로운 최소값이니까
    elif cur_num==ans: # 동일한 최소값이 나왔다면
        cnt +=1 # count
print(ans, cnt)


