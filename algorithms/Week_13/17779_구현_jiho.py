import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
N = int(input())
# pan = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
pan = [[]]
for _ in range(N):
    pan.append([0] + list(map(int,input().split())))

def mancount(x,y,d1,d2):
    count = [0,0,0,0,0]
    # 경계구역 설정
    fifth = [[0 for _ in range(N+1)] for i in range(N+1)]
    for i in range(d1+1):
        fifth[x+i][y-i] = 1 # 왼쪽, 위로 향하는 대각선
        fifth[x+d2+i][y+d2-i] = 1 # 오른쪽, 위로 향하는 대각선
    for j in range(d2+1):
        fifth[x+j][y+j] = 1 # 오른쪽, 아래로 향하는 대각선
        fifth[x+d1+j][y-d1+j] =1  #왼쪽, 아래로 향하는 대각선
    for i in range(x+1,x+d1+d2):
        flag = False
        for j in range(N+1):
            if fifth[i][j]==1:
                if flag==True:
                    flag=False
                else:
                    flag=True
            else:
                if flag==True:
                    fifth[i][j] = 1
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i < x+d1 and j <= y and fifth[i][j] != 1:
                count[0] += pan[i][j]
            elif i <= x+d2 and y < j and fifth[i][j] != 1:
                count[1] += pan[i][j]
            elif x+d1 <= i and j < y-d1+d2 and fifth[i][j] != 1:
                count[2] += pan[i][j]
            elif x+d2 < i and y-d1+d2 <= j and fifth[i][j] != 1:
                count[3] += pan[i][j]
            elif fifth[i][j]==1:
                count[4] += pan[i][j]
    return max(count) - min(count)

# 경계선 x,y,d1,d2를 정해야 함

# 1번 선거구: 1 ≤ r < x+d1, 1 ≤ c ≤ y
# 2번 선거구: 1 ≤ r ≤ x+d2, y < c ≤ N
# 3번 선거구: x+d1 ≤ r ≤ N, 1 ≤ c < y-d1+d2
# 4번 선거구: x+d2 < r ≤ N, y-d1+d2 ≤ c ≤ N
# 5번 선거구: 그 외의 나머지 + 경계선
min_count = float('inf')
for x in range(1, N+1):
    for y in range(1, N+1):
        for d1 in range(1, N+1):
            for d2 in range(1, N+1):
                if 1 <= x < x+d1+d2 <= N  and 1 <= y-d1 < y < y+d2 <= N:
                    min_count = min(min_count,mancount(x,y,d1,d2))

print(min_count)