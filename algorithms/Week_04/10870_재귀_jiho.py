import sys
from sys import stdin
sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

n = int(input())

# 리스트 초기화
d = [0]* 30

def fibo(n):
    if n<=1:
        return n
    if d[n] !=0: # 이미 계산된 것 있다면 그대로 반환
        return d[n]
    d[n] = fibo(n-1) + fibo(n-2)
    return d[n]
print(fibo(n))

