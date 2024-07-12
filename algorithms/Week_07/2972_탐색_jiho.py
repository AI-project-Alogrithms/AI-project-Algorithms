# 보석 상자
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def solution(start, end):
    while(start<=end):
        total = 0
        mid = (start+end)//2 # 한사람이 가져간 보석의 수
        for item in lst:
            if item%mid == 0: # 나누어 떨어지면
                total += (item//mid)
            else: # 홀수이면, 남은 사람이 나머지 구슬을 가지게 되는거니까
                total += (item//mid) + 1
        if total > N: # 인원이 기존 인원보다 많다면 한 사람당 가지고 있는 구슬 수 늘리기
            start = mid+1
        else:
            # 인당 가지는 개수 줄여보기 (최소값 구하는거니까)
            end = mid-1
    print(start)

# 가장 많은 보석을 가져간 학생이 가지고 있는 보석의 개수 => 질투심
# 총 학생 수 => 각 색상 별로 수 / 한사람이 가져간 보석의 수 의 합
# 총 학생수보다 더 많은 학생이 있다면 한사람이 가져간 보석의 수를 늘리기

N, M = map(int, input().split())
lst = []
for _ in range(M):
    lst.append(int(input()))

start = 1 # 한사람이 가져간 보석의 수 최소값
end =  max(lst) # 한사람이 가져간 보석의 수 최대값
solution(start, end)