def solution(A):
    visited = set()
    ans = 0
    for i, _ in enumerate(A):
        cur = i
        cnt = 0
        while cur not in visited:
            visited.add(cur)
            cur = A[cur]
            cnt += 1
        ans = max(ans, cnt)
    return ans




A = [5,4,0,3,1,6,2]
print(solution(A))