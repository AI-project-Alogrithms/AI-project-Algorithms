import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline


n, k = map(int, input().split())
lst = list(map(int, input().split()))
start, end = 0,0
dict_s = {key:0 for key in set(lst)}

ans = 0
while end < n:
    if dict_s[lst[end]]>=k:
        dict_s[lst[start]]-=1
        start+=1
    else:
        dict_s[lst[end]]+=1
        end+=1
        ans = max(ans, end-start)
# print(dict_s)
print(ans)