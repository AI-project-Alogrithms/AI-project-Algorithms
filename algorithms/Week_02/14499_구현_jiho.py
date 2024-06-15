import sys
from sys import stdin
sys.stdin=open("Week_02/input.txt","r")
input=sys.stdin.readline

# 세로, 가로, (현재 위치: 좌표x, 좌표y), 명령 개수 k
n,m,cx, cy,k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
k = [i-1 for i in list(map(int, input().split()))]

# 출력 확인
# print(f"n: {n}, m: {m}, x: {cx}, y: {cy}, k: {k}")
# print("arr:", arr)

# 동, 서, 북, 남
dx = [0,0,-1,1]
dy = [1,-1,0,0]
"""
주사위 기준을 잡아서 굴리기
"""
# 주사위 초기화 0
n1 = n2=n3=n4=n5=n6=0
alist = []
# 명령 방향대로 이동 후 처리
for dr in k:
    # 이동 후 범위 내이면 처리
    nx, ny = cx + dx[dr], cy + dy[dr]        
    if 0<= nx < n and 0<=ny<m:
        # 주사위 굴리기
        if dr == 0: # 동쪽이면 바뀌는 위치들 넣기
            n1,n3,n4,n6 = n4,n1,n6,n3
        elif dr == 1: # 서쪽이면
            n1,n3,n4,n6 = n3,n6,n1,n4
        elif dr == 2: # 북쪽이면
            n1,n2,n5,n6 = n5,n1,n6,n2
        else: # 남쪽이면
            n1,n2,n5,n6 = n2,n6,n1,n5
            
        # 이동한 바닥판이 0인지 여부에 따라 처리    
        if arr[nx][ny] == 0: # 이동한 칸에 쓰여있는 수가 0이면
            arr[nx][ny] = n6
        else: # 0이 아니면
            n6 = arr[nx][ny] # n6 <- arr copy
            arr[nx][ny] = 0
        alist.append(n1) # 윗면의 값을 추가
        cx, cy  = nx, ny
print("\n".join(map(str, alist)))
    
 

        
        

