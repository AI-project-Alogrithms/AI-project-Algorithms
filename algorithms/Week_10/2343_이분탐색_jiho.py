# 기타레슨
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def binary_search(lst):
    start, end = max(lst), sum(lst)
    while(start<=end):
        mid = (start+end)//2
        total = 0 # 한 구간 총합
        cnt = 1 # 전체 개수 => M과 동일할때까지 반복
        for t in lst:
            if total+t > mid:
                cnt +=1
                total = 0 # 다시 초기화 (다음구간으로)
            total += t
        if cnt <= M: # 구간 개수와 동일하다면 OR 더 적다면 더 최소값 찾기
            ans = mid
            end = mid-1
        else: # 정해진 구간보다 많다면 더 크게 만들기
            start = mid +1
    return ans
# 강의 수,
N, M = map(int, input().split())
lst = list(map(int, input().split()))

print(binary_search(lst)) # 이분 탐색
