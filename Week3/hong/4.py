def Jaden_Case(s):
    # 함수를 완성하세요
    list=s.split()
    res=""
    for a in list:
        low=a[1:].lower()
        up=a[0].upper()
        res=res+(up+low)+" "
    return res[:-1]      

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(Jaden_Case("3people unFollowed me for the last week"))
