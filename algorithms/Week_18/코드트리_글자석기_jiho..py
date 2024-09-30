# 그리디, 정렬
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline


# 문자열을 캐싱하여 중복 계산 최소화
def rfunc(s):
    return "".join(sorted(s, reverse=True))

def lfunc(s):
    return "".join(sorted(s))

n = int(input())
lst = [input().rstrip() for _ in range(n)]

# 정렬된 문자열을 미리 계산
sorted_lst = [(lfunc(s), rfunc(s)) for s in lst]
# print(sorted_lst)
# 모든 문자열에 대해 정렬된 결과 미리 계싼
entries = []
for i in range(n):
    entries.append((sorted_lst[i][0], i, False)) # 정렬된 버전
    entries.append((sorted_lst[i][1], i, True)) # 역순
# print(entries)
entries.sort()
# print(entries)

# 가장 빠른 순서 -> 하나만 sort, 나머지는 reverse
fast = [0] * n
r_cnt = 0
for st, index, is_rev in entries:
    # print(st, index, is_rev)
    # print(r_cnt)
    if is_rev:
        r_cnt+=1
    else:
        fast[index] = r_cnt+1
    # print(fast)

# 가장 느린 순서 -> 하나만 reverse, 나머지는 sort
last = [0] * n
f_cnt = 0
for st, index, is_rev in reversed(entries):
    if not is_rev: # 정렬되어 있다면
        f_cnt+=1
    else: # 역순이 맞다면
        last[index] = n-f_cnt # 사전순으로 느린 문자열의 수

for i in range(n):
    print(fast[i], last[i])


