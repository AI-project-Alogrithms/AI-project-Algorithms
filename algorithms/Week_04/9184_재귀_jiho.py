# 신나는 함수 실행
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def w(a,b,c):
    if a<=0 or b<=0 or c<= 0:
        return 1
    if a > 20 or b>20 or c>20:
        return w(20,20,20)
    # 반약 dp에 존재한다면 바로 출력
    if dp[a][b][c]:
        return dp[a][b][c]

    if a<b and b<c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][b]
    else:
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return dp[a][b][c]

dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]
while(True):
    a,b,c = map(int, input().split())
    if a==-1 and b==-1 and c==-1:
        break
    answer = w(a,b,c)
    print("w({}, {}, {}) = {}".format(a,b,c,answer))