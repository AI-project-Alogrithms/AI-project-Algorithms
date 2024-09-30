# 이분탐색 이용 문제
import sys
# sys.stdin = open("C:/Users/linda/OneDrive/바탕 화면/2024/AI-project-Algorithms/algorithms/input.txt", "r")
input = sys.stdin.readline

"""
대 k까지 사용할 수 있는 막대기의 길이를 최소로 하는 길이를 구하기
막대기로 오름차순으로 되어있는 3,4,7,9,... 이런식으로 구멍이 뚫려있는 곳을 막을때 다 막는 경우,
예를 들어 [1,3,6,7,8,9] 이렇게 구멍이 뚫려있으면 k가 3일때 최소 길이 3은 되야 모든 구멍을 막을 수 있음 (구멍을 막기 위해 막대기를 겹쳐도 됨) 
"""

def can_use(holes, mid, k):
    cnt = 1 # 막대 사용 처음에 한개 사용
    cur_point = holes[0] # 현재 구멍이 막은 위치 초기화
    for i in range(1, n):
        if holes[i] > cur_point+mid-1: # 현재 구멍 위치가 막대기 길이로 막을 수 없다면
            cnt +=1 # 막대기 추가
            cur_point = holes[i] # 막대기 위치 변경
    if cnt > k:
        return False
    return True

def binary_search(holes, k):
    start, end = 0, holes[-1]-holes[0]-1 # 최대 막대기 길이 = 구멍의 최대 간격
    ans = end
    while(start<=end):
        mid = (start+end)//2
        # 해당 막대기 길이로 k보다 작은 개수를 사용해서 구멍을 막을 수 있다면
        if can_use(holes, mid, k):
            ans = mid # 답을 해당 길이로 업데이트
            end = mid-1 # 길이를 줄여보기
        else:
            start = mid+1 # 길이 늘리기
    return ans


n, k = map(int, input().split())
holes = list(map(int, input().split()))
print(binary_search(holes, k))