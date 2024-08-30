# 영화 감독 숍 => 666이 있으면 번째를 cnt
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

n = int(input())
num = 666
cnt = 0

while(True):
    if '666' in str(num):
        cnt+=1 # n번째 더하기
    if cnt==n:
        break
    num+=1

print(num)