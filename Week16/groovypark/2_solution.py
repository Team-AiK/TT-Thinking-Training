def solution(phone_book):
    sorted_phone_book = sorted(phone_book)
    length = len(sorted_phone_book)
    for i in range(length-1):
        if (sorted_phone_book[i] in sorted_phone_book[i+1]):
                return False

    return True

print(solution(["911", "97625999", "91125426"]))