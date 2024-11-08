def solution(plans):
    answer = []

    for i in range(len(plans)):
        plans[i][1] = [int(plans[i][1][:2]), int(plans[i][1][3:])]
        plans[i][2] = [plans[i][1][0], plans[i][1][1] + int(plans[i][2])]
    # print(plans)
    for i in range(len(plans)):
        if plans[i][2][1] >= 60:
            plans[i][2] = [plans[i][2][0] + plans[i][2][1] // 60, int(plans[i][2][1] % 60)]

    plans.sort(key=lambda x: (x[1][0], x[1][1]))
    # print(plans)
    # 새로운 과제 -> 멈춘 과제 중 최신 순 start
    stack = []  # 멈춘 과제 쌓기
    target, start, end = plans[0]
    for nt, ns, ne in plans[1:]:
        if ns < end:
            stack.append(target)
            target, start, end = nt, ns, ne
        else:
            answer.append(target)
            target, start, end = nt, ns, ne
    answer.append(target)
    while stack:
        answer.append(stack.pop())
    # print(stack)
    # print(answer)
    return answer