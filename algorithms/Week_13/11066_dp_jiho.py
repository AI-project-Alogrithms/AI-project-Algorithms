# 파일 합치기
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
inf = int(10**9)
def solve():
    n = int(input())
    arr = [int(x) for x in input().split()]
    rst = [[0 for _ in range(n)] for _ in range(n)]
    for j in range(1,n): # 자기자신은 0으로 초기화, j가 뒤에 채워지고 i가 먼저 채워짐
        for i in range(j-1, -1, -1): # i는 j보다 하나 작은 것부터 시작 (AB)
            small = inf
            for k in range(j-i):
                small = min(small, rst[i][i+k]+rst[i+k+1][j])
            rst[i][j] = small + sum(arr[i:j+1])
    print(rst[0][-1])


t = int(input())
for _ in range(t):
    solve()
