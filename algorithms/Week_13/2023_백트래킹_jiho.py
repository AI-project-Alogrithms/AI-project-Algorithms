# 신기한 소수
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

# 소수 판별 함수
def is_prime_num(x):
    # 2~(x-1) 까지의 모든 수 확인
    for i in range(2,int(x**0.5)+1):
        # x가 해당수로 나누어 떨어진다면 false
        if x % i ==0:
            return False
    return True

def dfs(cnt, current_num):
    global ans
    if cnt==n: # 자리수 다 채워졌다면
        print(current_num)
        return

    for i in range(1,10):
        new_num = current_num*10+i
        if is_prime_num(new_num): # 소수라면 계속 진행
            dfs(cnt+1, new_num)

n = int(input())
ans = []
for first in [2,3,5,7]: # 첫자리 무조건 소수여야됨
    dfs(1, first)
# for word in ans:
#     print("".join(map(str, word)))
