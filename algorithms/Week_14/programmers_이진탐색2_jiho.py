# 징검다리
def solution(distance, rocks, n):
    rocks.sort()
    d = [0] * (len(rocks) + 1)
    d[0] = rocks[0]
    d[-1] = distance - rocks[-1]

    for i in range(1, len(rocks)):
        d[i] = rocks[i] - rocks[i-1]

    left, right = 0, distance

    while left <= right:
        mid = (left + right) // 2

        removed_stone = 0
        cur = 0

        for i in range(len(d)):
            cur += d[i]

            if cur < mid:
                removed_stone += 1
            else:
                cur = 0

        if removed_stone <= n:
            left = mid + 1
        elif removed_stone > n:
            right = mid -1
        # else:
        #     left = mid + 1

    return left -1
