def Jaden_Case(s):
    # 함수를 완성하세요
    list=s.split()
    res=[]
    for a in list:
        low=a[1:].lower()
        up=a[0].upper()
        res.append(up+low)
    return ' '.join(res)
