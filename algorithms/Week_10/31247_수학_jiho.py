# 2024는 무엇이 특별할까? => 수학공식 이용??
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def count_num(n,k):
    global ans
    while n and k:
        n //= 2
        k -= 1
    ans.append((n+1)//2)

T = int(input())
ans = []
for _ in range(T):
    n,k = map(int, input().split())
    count_num(n,k)

print("\n".join(map(str, ans)))
