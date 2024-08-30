# Hanyang Popularity Exceeding Competition
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline


def max_popularity(n, people):
    max_pop = 500  # P_i, C_i의 최대 값이 500이므로
    dp = [-1] * (max_pop + 1)
    dp[0] = 0  # 초기 인기도 0

    for P, C in people:
        # 뒤에서부터 앞으로 탐색해야 중복 갱신을 막을 수 있음
        for x in range(max_pop, -1, -1):
            if dp[x] != -1 and abs(P - x) <= C:
                dp[x + 1] = max(dp[x + 1], dp[x] + 1)

    return max(dp)


# 입력 처리
n = int(input())
people = [tuple(map(int, input().split())) for _ in range(n)]

# 결과 출력
print(max_popularity(n, people))
