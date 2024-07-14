# K번째 수
"""
중요한 것: K번째 수를 구하는 거니까, K번째를 바로 찾으려 하지 말기
수가 10억 이상이다 -> 이분 탐색
배열의 규칙 찾기
첫번째 행: 1X1, 1X2, 1X3,...,1XN
두번째 행: 2X1, 2X2, ... , 2XN
..
i번째 행: ix1, ix2, ... , ixN
=> 구하려는 수의 최대값, 최소값
min = 1 (1x1)
max = NXN
이 안에서 탐색을 진행해서 구하려는 수보다 작은 값들의 개수를 세기
구하려는 수보다 작은 값들의 개수는
각 행을 돌면서 min(mid/i, N) # 해당 열보다 벗어나면 안되니까
=> CNT 로 더하기
if cnt < k:
start = mid+1
else:
end = mid-1
return start # 작은 값들의 개수가 k와 동일하다면 해당 값을 반환

"""
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def search(n, k):
    start, end = 1, n*n # min값, max값
    while(start<=end):
        # print("start, end: ", start, end)
        mid = (start+end)//2
        # print("mid: ", mid)
        cnt = 0 # 전체 개수 더하기
        for i in range(1,n+1):
            cnt += min(mid//i, n)
        # print("cnt: ", cnt)
        if cnt < k:
            start = mid+1
            # print("start: ", start)
        else:
            end = mid-1
    return start


n = int(input())
k = int(input())

print(search(n, k))