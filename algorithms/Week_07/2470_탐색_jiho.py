# 두 용액 => 투 포인트 탐색
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

ans = abs(arr[0]+arr[-1]) # 초기화

p1,p2 = 0, len(arr)-1 # 양끝 인덱스로 초기화
final = [arr[p1], arr[p2]]
while(p1 < p2):
    tmp = arr[p1] + arr[p2]
    if abs(tmp) <= ans:
        ans = abs(tmp)
        final_ans = [arr[p1], arr[p2]]
        if ans == 0:
            break # 답
    if tmp < 0: # 값이 음수라면
        p1 +=1
    else:
        p2 -=1
print(final_ans[0], final_ans[1])