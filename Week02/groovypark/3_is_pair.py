def is_pair(s):
    # 함수를 완성하세요
    n = 0
    for text in s:
        if text == "(" and n >=0:
            n = n + 1
        if text == "(" and n < 0:
            return False
        if (text == ")" and n >= 0):
            n = n - 1
    if n == 0: return True
    else: return False

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( is_pair("(hello)()"))
print( is_pair(")("))