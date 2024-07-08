# 버블, 선택, 삽입, 퀵, 병합, 힙, 기수, 계수
import random


def bubble_sort(arr): # 바로 옆에 있는 것과 비교해서 정렬, 모든 인덱스에 대해 실행
    for i in range(len(arr)):
        for j in range(len(arr)-i-1): # index-1 만큼 두개씩 반복
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selection_sort(arr): # 배열에서 작은 데이터를 선별해서 데이터를 앞으로 보내는 정렬
    for i in range(len(arr)):
        min_index = i # 가장 작은 데이터의 인덱스라고 가정
        for j in range(i+1, len(arr)):
            # i 앞에 있는 데이터들에 대해서 돌동안
            if arr[min_index] > arr[j]:
                min_index = j # min_index보다 더 작은 값이 있다면 min_index 변경
        arr[i], arr[min_index] = arr[min_index], arr[i] # min_index 값을 가장 앞으로 보내기
    # 그러면 i번째 이후만 계속 확인하면 됨
    return arr

def quick_sort(arr): # 다른 원소와의 비교로 정렬 n개의 데이터 정렬 시, 평균 nlogn, 최악 n^2
    if len(arr)<=1: # 배열의 길이가 1이라면
        return arr #
    pivot = arr[len(arr)//2] # 배열의 중간 인덱스 값을 pivot으로 결정
    left, right,equal = [], [], [] # pivot의 left, right결정, 같다면 equal
    for i in arr: # 배열 돌동안
        if i<pivot: # pivot이 i보다 크다면
            left.append(i) # pivot의 left에 i 추가
        elif i > pivot: # i가 더 크다면 right에 추가
            right.append(i)
        else: #pivot값과 같다면 equal에 추가
            equal.append(i)
    return quick_sort(left) + equal + quick_sort(right) # 재귀 호출로 반복


def merge_sort(arr):
    print(f"merge_sort 호출됨: {arr}")  # 처음 배열 상태 출력
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2  # 배열의 중간 인덱스 설정
    print(f"중간 인덱스: {mid}, left: {arr[:mid]}, right: {arr[mid:]}")  # 중간 인덱스와 좌우 배열 출력

    left = merge_sort(arr[:mid])  # mid를 기준으로 left
    right = merge_sort(arr[mid:])  # mid를 기준으로 right

    print(f"left 정렬 후: {left}, right 정렬 후: {right}")  # 정렬된 좌우 배열 출력

    merge_arr = []  # 다시 합쳐질 배열
    l = r = 0
    while l < len(left) and r < len(right):  # 작은거 먼저 넣기
        if left[l] < right[r]:
            merge_arr.append(left[l])
            l += 1
        else:
            merge_arr.append(right[r])
            r += 1
        print(f"병합 중: {merge_arr}")  # 병합 중 상태 출력

    merge_arr += left[l:]  # 남은거 넣기
    merge_arr += right[r:]  # 남은거 넣기
    print(f"병합 완료: {merge_arr}")  # 병합 완료 상태 출력
    return merge_arr


# 예제 호출
# arr = [38, 27, 43, 3, 9, 82, 10]
# sorted_arr = merge_sort(arr)
# print(f"정렬된 배열: {sorted_arr}")

## heap 코드 다시 짜보기
def heap_sort(arr): # 최대 힙 트리(내림차순), 최소 힙 트리 구성(오름차순)해 정렬
    def heapify(arr, n, i): # 부모노가 항상 자식 노드보다 큰 이진트리
        largest = i # 현재 힙에서 가장 큰 값을 가진 노드의 인덱스.
        l = 2*i+1 # 현재 노드의 왼쪽 자식과 오른쪽 자식 인덱스.
        r = 2*i+2
        if l<n and arr[i]<arr[l]:
            largest = l
        if r<n and arr[largest]<arr[r]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)
        print(f"Heapify 단계: {arr}")  # 힙 구성 중 상태 출력

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        print(f"루트와 교환: {arr}")  # 루트와 마지막 요소 교환 후 상태 출력
        heapify(arr, i, 0)
        print(f"Heapify 재호출 후: {arr}")  # 힙 재구성 후 상태 출력

    return arr

def radix_sort(arr): # 기수 정렬 - 정수, 낱말, 등 사전순 정렬
    RADIX = 10
    placement = 1

    max_digit = max(arr)

    while placement < max_digit:
        buckets = [list() for _ in range(RADIX)]

        for i in arr:
            tmp = int((i / placement) % RADIX)
            buckets[tmp].append(i)

        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                arr[a] = i
                a += 1

        placement *= RADIX

    return arr

def count_sort(arr): # 계수 정렬, 작은 양의 정수들인 키에 따라 정렬
    max_value = max(arr)
    m = max_value + 1
    count = [0] * m

    for a in arr:
        count[a] += 1

    i = 0
    for a in range(m):
        for c in range(count[a]):
            arr[i] = a
            i += 1
    return arr


arr = [i for i in random.sample(range(10), 10)]

"""
merge_sort 호출됨: [38, 27, 43, 3, 9, 82, 10]
중간 인덱스: 3, left: [38, 27, 43], right: [3, 9, 82, 10]
merge_sort 호출됨: [38, 27, 43]
중간 인덱스: 1, left: [38], right: [27, 43]
merge_sort 호출됨: [38]
merge_sort 호출됨: [27, 43]
중간 인덱스: 1, left: [27], right: [43]
merge_sort 호출됨: [27]
merge_sort 호출됨: [43]
left 정렬 후: [27], right 정렬 후: [43]
병합 중: [27]
병합 완료: [27, 43]
left 정렬 후: [38], right 정렬 후: [27, 43]
병합 중: [27]
병합 중: [27, 38]
병합 완료: [27, 38, 43]
merge_sort 호출됨: [3, 9, 82, 10]
중간 인덱스: 2, left: [3, 9], right: [82, 10]
merge_sort 호출됨: [3, 9]
중간 인덱스: 1, left: [3], right: [9]
merge_sort 호출됨: [3]
merge_sort 호출됨: [9]
left 정렬 후: [3], right 정렬 후: [9]
병합 중: [3]
병합 완료: [3, 9]
merge_sort 호출됨: [82, 10]
중간 인덱스: 1, left: [82], right: [10]
merge_sort 호출됨: [82]
merge_sort 호출됨: [10]
left 정렬 후: [82], right 정렬 후: [10]
병합 중: [10]
병합 완료: [10, 82]
left 정렬 후: [3, 9], right 정렬 후: [10, 82]
병합 중: [3]
병합 중: [3, 9]
병합 완료: [3, 9, 10, 82]
left 정렬 후: [27, 38, 43], right 정렬 후: [3, 9, 10, 82]
병합 중: [3]
병합 중: [3, 9]
병합 중: [3, 9, 10]
병합 중: [3, 9, 10, 27]
병합 중: [3, 9, 10, 27, 38]
병합 중: [3, 9, 10, 27, 38, 43]
병합 완료: [3, 9, 10, 27, 38, 43, 82]
정렬된 배열: [3, 9, 10, 27, 38, 43, 82]

Process finished with exit code 0

"""