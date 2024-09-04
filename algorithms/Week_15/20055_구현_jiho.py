# 컨베이너 벨트 위의 로봇
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

N, K = map(int, input().split())
lst = list(map(int, input().split()))
robot = [0]*N
ans = 0 # 몇회
cnt = 0
while(True):
    ans += 1
    # 회전: 로봇 회전, N+1로봇 내림
    # lst = [lst[-1]]+lst[:-1] # 296mS: 느림
    # robot = [0] +robot[:-1]
    # robot[N-1] = 0
    lst.insert(0,lst.pop()) # 제일 끝을 꺼내서 앞에 넣기 232mS
    robot.pop()
    robot.insert(0,0) # 앞에 0을 넣어줌
    robot[N - 1] = 0


    # 로봇 이동
    for i in range(N-2, 0, -1):
        if robot[i]==1 and robot[i+1]==0 and lst[i+1]>0:
            robot[i], robot[i+1] = 0, 1
            lst[i+1]-=1
            if lst[i+1]==0:
                cnt+=1

    # 로봇 채우기 (0자리 내구도 >0, 이면 )
    if lst[0]>0:
        robot[0] = 1
        lst[0] -=1
        if lst[0] == 0:
            cnt += 1

    # lst에서 0개수 세기
    # if lst.count(0) >= K: # 매번 0의 개수를 COUNT -> 느림
    #     break
    # 내구도가 감소해서 0이되면 cnt +=1
    if cnt >=K: # 200mS => 이게 더 빠름
        break
print(ans)
