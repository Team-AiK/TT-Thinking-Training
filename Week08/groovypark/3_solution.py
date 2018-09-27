def update(the_list, n, result):
    templist = the_list[n:]
    templist.sort()
    the_list = the_list[:n] + templist
    result.append(the_list.copy())
    return the_list


def perm(num):
    source = [x for x in range(1, int(num) + 1)]
    resource = [x for x in range(int(num), 0, -1)]
    result = [source.copy()]

    while source != resource:
        for i in range(len(source) - 1, 0, -1):
            if source[i] > source[i - 1]:
                for j in range(i, len(source)):
                    if source[i - 1] > source[j]:
                        temp = source[i - 1]
                        source[i - 1] = source[j - 1]
                        source[j - 1] = temp
                        source = update(source, i, result)
                        break
                    elif j == len(source) - 1:
                        temp = source[i - 1]
                        source[i - 1] = source[j]
                        source[j] = temp
                        source = update(source, i, result)
                        break
                break
    return result


def solution(n, k):
    result = perm(n)
    return result[k-1]


print(solution(3, 5))
