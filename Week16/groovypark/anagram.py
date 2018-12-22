def solution(A, B):
    sorted_A = sorted(A)
    sorted_B = sorted(B)

    if len(A) != len(B):
        return False

    for i in range(len(A)):
        if sorted_A[i] != sorted_B[i]:
            return False

    return True

N = int(input())
for _ in range(N):
    A, B = input().split()
    if solution(A, B):
        print(A, '&', B, 'are anagrams.')
    else:
        print(A, '&', B, 'are NOT anagrams.')


# from collections import Counter

# def solution(A, B):
#     return Counter(A) == Counter(B)