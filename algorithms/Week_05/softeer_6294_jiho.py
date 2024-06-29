# 성적평균
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

N,K = map(int, input().split())

lst = list(map(int, input().split()))
lst = [0] +lst
for i in range(K):
    a, b = map(int, input().split())
    print("{:.2f}".format(round(sum(lst[a:b+1])/(b-a+1), 2)))

