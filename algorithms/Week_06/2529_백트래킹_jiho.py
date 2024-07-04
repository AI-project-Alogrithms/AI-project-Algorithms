# 부등호
import sys
from sys import stdin
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def check(left, right, item): # lst[-1], i, item[depth-1]
    if item == "<":
        return left<right # 문자열 비교는 사전순이라 int형 안바꾸고 해도됨
    else:
        return left>right


def dfs(n, lst):
    global min_v, max_v # final,
    if n==k+1:
        # 처음 생성: 최솟 값
        if len(min_v) == 0: # 어짜피 작은 것부터 순서대로 담기니까!! 똑똑쓰..
            min_v = lst
        # 마지막 담기는게 가장 최댓값
        else:
            max_v = lst
        return
    for i in range(10):
        if not visited[i]:
            if n==0 or check(lst[-1], str(i), item[n-1]):
                # 처음 입력일때, check 조건이 true 일때 넣기
                visited[i] = True
                dfs(n+1, lst+str(i))
                visited[i] = False


k = int(input())
item = list(input().rstrip().split())
visited = [False]*10
min_v = ""
max_v = ""
dfs(0, "") # n, lst -> string 그대로 더해도 됨!
print(max_v)
print(min_v)