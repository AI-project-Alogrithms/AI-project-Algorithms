# 한 수
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def func(num):
    global cnt
    flag = True
    tmp = list(str(num))
    ans = int(tmp[0]) - int(tmp[1])
    for i in range(len(tmp) - 1):
        if ans != int(tmp[i]) - int(tmp[i + 1]):
            flag = False
            break
    if flag==True:
        cnt+=1

n = int(input())
# 두자리 수까지 모두 한 수
if n<=99:
    cnt = n
    # print(n)
else:
    cnt = 99
    for i in range(100,n+1):
        func(i)
print(cnt)
