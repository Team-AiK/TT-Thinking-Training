# 앞뒤를 뒤집어도 똑같은 문자열을 palindrome이라고 합니다.
# longest_palindrom함수는 문자열 s를 매개변수로 입력받습니다.
# s의 부분문자열중 가장 긴 palindrom의 길이를 리턴하는 함수를 완성하세요.
# 예를들어 s가 "토마토맛토마토"이면 7을 리턴하고 "토마토맛있어"이면 3을 리턴합니다.

def longest_palindrom(s):
    result = []
    for i in range(len(s)):
        for j in range(1,len(s)+1):
            if s[i:j] == s[i:j][::-1]:
                result.append(len(s[i:j]))
            if s[j:i] == s[j:i][::-1]:
                result.append(len(s[j:i]))
    return max(result)

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(longest_palindrom("토마토맛토마토"))
print(longest_palindrom("토마토맛있어"))