# 감소하는 수 => 서로 다른 수들의 조합
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline
from itertools import combinations


N = int(input())
ans = []
for i in range(1,11): # 1부터 10의 자리수까지 반복
    for j in combinations(range(10),i): # 0~9까지 숫자를 i자리 수만큼 조합 생성
        num = sorted(list(j), reverse=True) # 역순 정력
        ans.append(int("".join(map(str, num))))
ans.sort()# 리스트 자체 정렬
if len(ans)>N:
    print(ans[N])
else:
    print(-1)



