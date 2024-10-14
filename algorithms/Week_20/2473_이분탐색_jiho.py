# 세 용액
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def binary_search(point):
    global ans, result
    start, end = point+1, N-1 # 인덱스
    while(start<end):
        if point==start:
            start+=1
            continue
        if point==end:
            end-=1
            continue
        t = lst[point]+lst[start]+lst[end]
        if abs(t)<ans:
            ans = abs(t)
            result = [lst[point], lst[start], lst[end]]
            # print(result)
        if t<0:
            start+=1
        elif t>0:
            end-=1
        else:
            break


N = int(input())
lst = list(map(int, input().split()))
lst.sort()
# print(lst)

ans = sys.maxsize # 최종 가장 작은 수
result = []
for i in range(N-2):
    binary_search(i)
print(" ".join(map(str, result)))
