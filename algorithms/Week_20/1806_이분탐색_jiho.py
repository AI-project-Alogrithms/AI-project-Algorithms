# 부분합
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

N, S = map(int, input().split())
lst = list(map(int, input().split()))

if max(lst)>=S:
    print(1)
elif sum(lst)<S:
    print(0)
else:
    # print(lst)
    ans = N
    start, end = 0, 1
    tmp = sum(lst[start:end + 1])
    while (start<end):
        if tmp<S:
            if end==N-1:break
            end+=1
            tmp+=lst[end]
        else:
            if end-start+1<ans:
                ans = end-start+1
                if ans==2:
                    break
            tmp-=lst[start]
            start+=1

    print(ans)

