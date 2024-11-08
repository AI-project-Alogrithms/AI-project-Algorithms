def quick_sort(array):
    if len(array)<=1: # 리스트가 하나 이하의 원소 가지면 그대로 반환
        return array
    # 피벗
    pivot = array[len(array)//2]
    left = [x for x in array if x<pivot]
    middle =[x for x in array if x==pivot]
    right = [x for x in array if x>pivot]
    # 재귀 정렬
    return quick_sort(left)+middle+quick_sort(right)

array = [3,6,8,10,1,2,1]
sorted_array = quick_sort(array)
print(sorted_array)