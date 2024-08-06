# 모바일 광고 입찰: 이분 탐색 -> 10억 이상
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def binary_search():
    start, end = 0, 10**9

    while(start <=  end):
        mid = (start+end)//2
        cnt = 0
        # print(mid)
        for a, b in lst:
            if a+mid >= b:
                cnt +=1
        if cnt>=K:
            end = mid-1
        else:
            start = mid+1
    return start


N, K = map(int, input().split())
cnt = 0
lst = []
for _ in range(N):
    a,b = map(int, input().split())
    lst.append([a,b])
    if a>= b:
        cnt +=1

if cnt >= K:
    print(0)
else:
    print(binary_search())