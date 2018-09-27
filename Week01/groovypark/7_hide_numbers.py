def hide_numbers(s):
    #함수를 완성해 별이를 도와주세요
    return '*' * (len(s)-4) + s[len(s)-4:]
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : " + hide_numbers('01033334444'));