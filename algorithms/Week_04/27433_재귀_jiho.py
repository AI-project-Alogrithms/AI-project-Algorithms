import sys
from sys import stdin
sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

n = int(input())

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(n))

