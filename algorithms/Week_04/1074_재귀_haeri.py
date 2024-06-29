import sys
input = sys.stdin.readline
count = 0

def f(x,y, step):
    global count
        
    # r, c가 해당 영역이 아닐 때 한 번에 count 더하기 (이 코드 없으면 시간초과)
    if r<x or r>=x+step or c<y or c>=y+step:
        count += step*step
        return
    
    # Z 찾기
    if step == 2:
        for i in range(2):
            for j in range(2):
                if r==x+i and c==y+j:
                    print(count)
                count += 1
        return    
    
    # 4등분으로 나눠 찾기
    for i in range(2):
        for j in range(2):
            # 4등분의 시작 x 좌표, 4등분의 시작 y 좌표, 움직이는 윈도우 크기
            f(x + int(step/2)*i, y + int(step/2)*j, int(step/2)) 

N, r, c= map(int, input().split())
f(0,0,2**N)