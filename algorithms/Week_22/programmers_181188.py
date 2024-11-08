def solution(targets):
    targets.sort(key=lambda x: x[1])
    # print(targets)
    cnt = 1
    s, e = targets[0]
    for start, end in targets[1:]:
        if start >= e:  # 현재 카메라가 커버할 수 없으면
            cnt += 1
            e = end

    return cnt