import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def binary_search(lst):
    start, end = 0, lst[-1]*M+1 # 심사를 하는데 걸리는 최소 시간
    while(start<=end):
        cnt = 0 # 사람 수
        mid = (start+end)//2
        for i in lst:
            cnt += mid//i
        if cnt<M:
            start = mid+1
        else:
            end = mid-1
    # print(start)
    return start

N, M = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(int(input()))
lst.sort()
ans = (10**9)**2
print(binary_search(lst))