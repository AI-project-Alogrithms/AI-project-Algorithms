# 좋다
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def search(point, ans):
    start = 0
    end = len(lst)-1
    while(start<end):
        if start == point:
            start+=1
            continue
        if end == point:
            end -=1
            continue
        tmp = lst[start]+lst[end]
        if tmp == ans:
            return 1
        if tmp < ans:
            start +=1
        else:
            end -=1
    return 0

n = int(input())
lst = list(map(int, input().split()))
lst.sort()
if n<3:
    print(0)
else:
    cnt = 0
    for i in range(n): # 근데 왜 2, n까지 하는게 오류일까 ==> 아 이건 음수일대를 고려안한거임. 음수일땐 앞에 있는 수를 더해도 해당 값이 나올수잇음
        cnt += search(i, lst[i])
    print(cnt)