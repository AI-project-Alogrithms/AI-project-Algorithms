
import sys
sys.stdin=open("./Desktop/input.txt","r")
input=sys.stdin.readline

T = int(input())


''' 풀이 1: 시간 초과: O(N^2) = N 2만 * M 2만 = 4억
for _ in range(T):
    N, M = map(int, input().split())
    A_list = list(map(int, input().split()))
    B_list = list(map(int, input().split()))
    answer = 0
    for i in range(N):
        for j in range(M):
            if A_list[i] > B_list[j]:
                answer += 1
    print(answer)
'''

# 풀이 2: bisect 라이브러리 이용 (이분 탐색)
import bisect

def count_less_than(lst, x): #
    index = bisect.bisect_left(lst, x) # lst에서 x보다 작은 원소의 개수 반환
    return index

for _ in range(T): # 시간초과: 2만*2만=4억
    N, M = map(int, input().split())
    A_list = list(map(int, input().split()))
    A_list = sorted(A_list)
    B_list = list(map(int, input().split()))
    B_list = sorted(B_list)
    
    answer = 0
    for A in A_list:
        answer += count_less_than(B_list, A)
    print(answer)