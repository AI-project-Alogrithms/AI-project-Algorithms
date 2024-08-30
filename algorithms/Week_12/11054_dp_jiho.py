# 가장 긴 바이토닉 부분 수열 ==> 풀기
import sys
sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
numlst = [
    [(0,1),(1,0),(1,2),(3,0),(3,2),(4,1)]
]
arr = [[0]*3 for _ in range(5)]

for i,j in numlst[0]:
    arr[i][j]=1
for i in arr:
    print(i)
