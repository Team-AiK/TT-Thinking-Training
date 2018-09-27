def adder(a, b):
    # 함수를 완성하세요
    if a > b:
      max = a
      min = b
    if a < b:
      max = b
      min = a
    list = [ x for x in range(min,max+1) ]

    # 다른사람 코드
    # return sum(range(min(a,b), max(a,b)+1))

    return sum(list)

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( adder(3, 5))