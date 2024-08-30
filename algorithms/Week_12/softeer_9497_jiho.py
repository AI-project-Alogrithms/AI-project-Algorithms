# Recovering the Region
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

n = int(input().rstrip())
for i in range(n):
    print(' '.join(map(str,[i+1]*n)))


