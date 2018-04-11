# def toWeirdCase(s):
#     # 함수를 완성하세요
#     list = s.split(' ')
#     result = []
#     for word in list:
#       for alphabet in word:
#         if word.index(alphabet)%2 == 0:
#           alphabet = alphabet.upper()
#       result.append(word)
#     return " ".join(result)

def toWeirdCase(s):
    def change(t):
        result = ""
        for i, v in enumerate(t):
            if i % 2:  # 홀수
                result += v.lower()
            else:  # 짝수
                result += v.upper()
        return result
    return ' '.join(list(map(change, s.split())))

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(toWeirdCase("try hello world")));