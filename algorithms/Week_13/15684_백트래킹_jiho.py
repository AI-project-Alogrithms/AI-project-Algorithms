import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def check(): # i열이 i번째에 도착하는지 확인
    for start in range(N): # 열 돌면서
        now = start # 첫번째 열부터 끝까지 돌기
        for j in range(H): # 행 돌기
            if arr[j][now]: # 사다리가 있다면
                now+=1 #오른족으로 이동
            elif now >0 and arr[j][now-1]: # 왼쪽에 사다리가 있다면
                now -= 1
        if start != now: # 자기자신으로 돌아오지 않았다면
            return False
    return True


def dfs(cnt, x, y):
    global ans
    if check(): # 각 자리가 자리 위치로 갔다면
        ans = min(ans, cnt) # 최솟값 업데이트
        return
    elif cnt ==3 or cnt >= ans:
        # 3과 동일하거나, 최소 횟수를 넘어가면
        return

    for i in range(x, H): # 각 행을 돌면서
        if i==x:
            now = y
        else:
            now = 0
        for j in range(now, N-1): # 마지막 열전까지 돌아야됨
            if not arr[i][j] and not arr[i][j+1]: # 오른쪽에 사다리 없다면
                if j>0 and arr[i][j-1]: # 범위내, 왼쪽에 사다리 있다면 패쓰
                    continue
                arr[i][j] = True # 사다리 설치
                dfs(cnt+1, i,j+2)
                arr[i][j] = False # 사다리 해제


# 세로선 개수, 가로선 개수, 위치
N, M, H = map(int, input().split())
arr = [[False]*N for _ in range(H)] # 배열 생성
for _ in range(M):
    a,b = map(int, input().split())
    arr[a-1][b-1] = True
ans = 4 # 최소값
dfs(0,0,0)
print(ans if ans < 4 else -1) # 3이하면 ans반환 아니면 -1반환