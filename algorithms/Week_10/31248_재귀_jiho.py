# 3+1 하노이 탑
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def move(tiles, s, e):
    if tiles == 0:
        return
    move(tiles-1, s, 3-s-e)
    print('ABC'[s], 'ABC'[e])
    move(tiles-1, 3-s-e, e)

N = int(input())
dp = [0,1]
for i in range(2,21):
    dp.append(2**(i-2)-1+3+dp[i-2])
print(dp[N]) # N개의 탑이 들어왔을때 최소 이동 수

pos = 0
while(N>=2):
    move(N-2, pos, 2-pos)
    print('ABC'[pos], 'B')
    print('ABC'[pos], 'D')
    print('B', 'D')

    N -= 2
    pos = 2-pos
if N==1:
    print('ABC'[pos], 'D')

