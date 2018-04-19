def longest_palindrom(s):
    # 함수를 완성하세요
    if s==s[::-1]:
        return len(s)
    return max(longest_palindrom(s[:-1]),longest_palindrom(s[1:]))


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(longest_palindrom("토마토맛토마토")) #7
print(longest_palindrom("토마토맛있어"))#3
print(longest_palindrom("저기저사람여보게저기저게보여"))#9
