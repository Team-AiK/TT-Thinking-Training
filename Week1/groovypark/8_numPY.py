def numPY(s):
    # 함수를 완성하세요
    pNum = s.count('p')+s.count('P')
    yNum = s.count('y')+s.count('Y')
    
    if pNum==yNum:
        return True
    else:
        return False

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( numPY("pPoooyY") )
print( numPY("Pyy") )