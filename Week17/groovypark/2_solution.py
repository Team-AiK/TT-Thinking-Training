def calculate(length, N):
    length.append(length[-1] + length[-2])
    if len(length) == N:
        return (length[-1] + length[-2] * 2 + length[-3]) * 2
    return calculate(length, N)


def solution(N):
    length = [1,1]

    return calculate(length, N)

print(solution(5))