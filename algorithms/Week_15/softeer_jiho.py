import sys
import bisect
input = sys.stdin.readline

n, q = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
setlst = set(lst) # 미리 만들어 두기 set으로
for _ in range(q):
    qa = int(input())
    if qa not in setlst:
        print(0)
    else:
        idx = bisect.bisect_left(lst, qa) # 이진탐색으로 찾기
        # print(idx)
        print(idx*((n-1)-idx))