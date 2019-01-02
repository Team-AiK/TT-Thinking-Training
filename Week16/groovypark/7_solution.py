def solution(citations):
    sorted_c = sorted(citations,reverse=True)
    for i in range(len(sorted_c)):
        if sorted_c[i] < i+1:
            return i
    return len(citations)

    # n = len(citations)
    # more_than = [0 for x in range(10001)]
    # less_than = [0 for x in range(10001)]
    
    # for citiation in citations:
    #     for i in range(citiation+1):
    #         less_than[i] += 1
            
    # for citiation in citations:
    #     for i in range(citiation, 10001):
    #         more_than[i] += 1
    
    # for i in range(n+1, -1, -1):
    #     if i >= more_than[i] and i <= less_than[i]:
    #         return i

print(solution([0,1,2,3,6,7,8,9,12,35,55]))