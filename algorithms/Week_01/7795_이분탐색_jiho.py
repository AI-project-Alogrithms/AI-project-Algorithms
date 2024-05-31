import bisect
import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    a_list.sort(reverse=True)
    b_list.sort()
    # print(a_list)
    # print(b_list)
    count = 0
    for i in a_list:
        # bisect_left를 사용하여 i보다 작은 b_list의 원소 개수를 찾음 (특정 원소가 들어갈 수 있는 가장 왼쪽 위치(인덱스)를 반환)
        count += bisect.bisect_left(b_list, i)
    # for i in a_list:
    #     for j in b_list:
    #         if i > j:
    #             count +=1
    print(count)