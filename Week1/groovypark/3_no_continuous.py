def no_continuous(s):
    # 함수를 완성하세요
    result = []

    if len(s) == 0:
      pass
    else:
      result = [s[0]]
    for i in range(1,len(s)):
      if s[i-1] == s[i]:
        pass
      else:
        result.append(s[i])
    return result

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( no_continuous( "133303" ))