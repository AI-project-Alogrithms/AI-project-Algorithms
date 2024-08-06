import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def func(lst, dp):
    # lst[0]: 칼로리, lst[1]: 가격
    for i in range(1, m+1): # 돈
        for j in range(n): # 사탕 종류
            if i<lst[j][1]: continue
            dp[i] = max(dp[i], dp[i-lst[j][1]]+lst[j][0])
    return dp[-1]


while True:
    n, m = map(str, input().rstrip().split())
    n = int(n)
    m = int(float(m) * 100 + 0.5) # 소수점 이하 두 자리를 고려하여 정수로 변환
    if n == 0 and m == 0: break # 종료 조건

    lst = []
    for _ in range(n):
        c, p = map(str, input().rstrip().split())
        c = int(c)
        p = int(float(p) * 100 + 0.5) # 소수점 이하 두 자리를 고려하여 정수로 변환
        lst.append((c, p))

    dp = [0] * (m + 1) # 최대값 저장
    print(func(lst, dp))
