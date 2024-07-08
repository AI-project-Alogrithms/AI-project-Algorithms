# 듣보잡 => 교집합 구하기
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())
n_list = set()
m_list = set()
for _ in range(n):
    n_list.add(input().rstrip())
for _ in range(m):
    m_list.add(input().rstrip())
ans = sorted(n_list & m_list)
print(len(ans))
print("\n".join(map(str, ans)))


