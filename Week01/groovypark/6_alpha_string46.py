def alpha_string46(s):
    # s의 길이가 4혹은 6이고, 숫자로만 구성되있는지 확인해주는 함수를 완성하세요.
    if (len(s)==4 or len(s)==6) and s.isdigit() :
        return True
    else:
        return False


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( alpha_string46("a234") )
print( alpha_string46("1234") )