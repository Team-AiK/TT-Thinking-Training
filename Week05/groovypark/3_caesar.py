# 시저 암호 Level 3
# 어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다.
# A를 3만큼 밀면 D가 되고 z를 1만큼 밀면 a가 됩니다. 공백은 수정하지 않습니다.
# 보낼 문자열 s와 얼마나 밀지 알려주는 n을 입력받아 암호문을 만드는 caesar 함수를 완성해 보세요.
# “a B z”,4를 입력받았다면 “e F d”를 리턴합니다.

def caesar(s, n):
    capital = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    small = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    result = []
    for i in range(len(s)):
        if s[i] in capital:
            index = capital.index(s[i])
            result.append(capital[(index+n)%26])
        if s[i] in small:
            index = small.index(s[i])
            result.append(small[(index+n)%26])
        if s[i] == " ":
            result.append(" ")
    return "".join(result)


# 실행을 위한 테스트코드입니다.
print('s는 "a B z", n은 4인 경우: ' + caesar("a B z", 4))