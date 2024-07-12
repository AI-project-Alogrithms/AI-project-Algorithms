# 선형, 이분(이진), 해시, 완전, 브루트포스, 백트래킹, 재귀
"""
10억 이상, 위치 구하기 이면 => 이분탐색
1. start, end 찾기
2. 분할 조건 찾기
3. 종료 조건 찾기
4. 부등호, 범위 잘 보기!!

"""
# 선형 탐색: 순서대로 하나씩 찾는 방법
def linear_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return None

# 이진 탐색: 반씩 제외하면서 찾기
def binary_search(list, target):
    first = 0
    last = len(list)-1 # 인덱스 번호
    while(first<=last):
        mid = (first+last)//2 # 리스트 가운데 인덱스
        if list[mid] == target: # 현재 위치가 target과 동일하다면
            return mid
        elif list[mid] < target:
            first = mid+1 # target값이 mid보다 크다면 mid보다 큰 위치부터 다시 탐색
        elif list[mid] > target:
            last = mid-1 # target값이 mid보다 작다면 mid보다 작은 위치까지만 다시 탐색
    return None

# 해시 탐색: 값과 인덱스 미리 연동 (딕셔너리)
def hash_search(list, target):
    hash_tabel = {} # 딕셔너리 생성
    for i in range(len(list)):
        hash_tabel[list[i]] = i # key: 리스트 값, value: index
    if target in hash_tabel:
        # 해당 값이 key에 존재한다면
        return hash_tabel[target] # 그때의 index 반환
    return None

# 완전 탐색 - 브루트 포스 (백트래킹, 재귀함수)
def brute_force_search(list, target):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] + list[j] == target:
                return [i,j]
    return None

def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else: # list가 존재한다면
        mid = len(list)//2
        if list[mid] == target:
            return True
        else:
            if list[mid] < target:
                return recursive_binary_search(list[mid+1:], target)
            else:
                return recursive_binary_search(list[:mid], target)

print(linear_search([1,2,3,4,5], 5))

print(binary_search([1,2,3,4,5], 5))

print(hash_search([1,2,3,4,5], 5))

print(brute_force_search([1,2,3,4,5], 5))

print(recursive_binary_search([1,2,3,4,5], 5))