# 게리맨더링 2
import sys
sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
print(arr)
# 인구가 가장 많은 선거구와 가장 적은 선거구의 인구 차이의 최솟값