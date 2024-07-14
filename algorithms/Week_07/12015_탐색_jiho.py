# 가장 긴 증가하는 수열 => 이건 해도해도 어렵냐
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def search(item): # l은 이미 정렬된 리스트임
    start = 0 # 인덱스 첫번째 값 (l의)
    end = len(l) - 1 # l의 인덱스 마지막 값
    while(start<=end):
        mid = (start + end) //2
        if l[mid] == item: # l의 해당 인덱스 값이 item과 동일하다면
            return mid # 해당 인덱스 값을 반환
        elif l[mid]<item: # item값이 해당 인덱스 값보다 크다면
            start = mid+1 # 더 큰쪽에서 찾기
        else:
            end = mid-1 # 해당 인덱스 값보다 item이 작다면 더 작은쪽에서 찾기
    return start

n = int(input())
lst = list(map(int, input().split()))

l = [lst[0]]
for item in lst:
    if l[-1]<item: # item이 l(가장 긴 수열)의 가장 큰 값보다 크다면
        l.append(item) # 가장 큰 값을 추가
    else:
        idx = search(item) # 가장 작은 인덱스 찾기
        l[idx] = item # 대체
print(len(l))