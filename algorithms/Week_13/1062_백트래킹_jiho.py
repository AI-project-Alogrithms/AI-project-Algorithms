# 가르침
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

def check():
    cnt = 0
    for word in wordlst:
        flag = True
        for s in word:
            if not alpha[ord(s)-97]:
                flag = False
                break
        if flag:
            cnt+=1
    return cnt

def dfs(start, cnt):
    global ans
    if cnt==K: # 최대 개수가 됐다면 단어 만들 수 있는 개수 확인 후 업데이트
        ans = max(ans, check())
        return
    for i in range(start, 26): # 알파벳 처음부터 읽기
        if not alpha[i]: # 아직 읽지 않은 알파벳이라면
            alpha[i] = True
            # 단어 하나씩 집어넣어보기
            dfs(i, cnt+1)
            alpha[i] = False

N, K = map(int, input().split())
alpha = [False for _ in range(26)] # 알파벳 존재 여부
wordlst =[input().rstrip() for _ in range(N)] # 단어 주어짐

ans = 0 # 최대 단어 개수
if K<5: # 기존 디폴트 보다 작으면
    print(0)
elif K==26: # 읽을 수 있는 알파벳 수가 전체이면
    print(N) # 전체 단어 다 읽을 수 있음
else:
    for c in ('a','n','t','i','c'):
        alpha[ord(c)-ord('a')] = True # 알파벳 존재 초기화, 97
    dfs(0,5) # 단어 읽기, cnt
    print(ans)
