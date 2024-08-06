# 이항계수3
# 이항계수란? 주어진 집합에서 원하는 개수만큼 순서없이 뽑는 조합의 개수
# 이항: 한개의 아이템에 대해서 뽑거나, 뽑지 않거라
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
INF = 1000000007 # 나눌 값

def bino_coef(n,k):
    cache = [[0 for _ in range(k+1)] for _ in range(n+1)]


n, k = map(int, input().split())
bino_coef(n,k)