# 입국심사
def solution(n, times):
    answer = 10 ** 9 * n  # 초기화
    times.sort()
    start, end = 1, times[-1] * n
    # print(times)
    while (start <= end):
        mid = (start + end) // 2
        cnt = 0  # 사람 수
        for t in times:
            cnt += mid // t
        if cnt < n:  # 사람을 모두 심사하지 못했으면 시간 늘리기
            start = mid + 1
        else:  # 모두 심사했다면
            # if cnt==n: # 인원수만큼 했다면
            answer = min(answer, mid)  # 더 많은 인원수를 해도 최소값이라면 갱신
            end = mid - 1
    # print(answer)

    return answer