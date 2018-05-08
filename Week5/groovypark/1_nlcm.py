# N개의 최소공배수 Level 3
# 두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다. 
# 예를 들어 2와 7의 최소공배수는 14가 됩니다. 
# 정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다. 
# nlcm 함수를 통해 n개의 숫자가 입력되었을 때, 최소공배수를 반환해 주세요. 
# 예를들어 [2,6,8,14] 가 입력된다면 168을 반환해 주면 됩니다.

def nlcm(num):
    
    while len(num) > 1:
        
        num.append(lcm(num[0],num[1]))
        num.pop(0)
        num.pop(0)
        

    return num[0]

def gcd(a,b):
    mod = a % b
    while mod > 0:
        a = b
        b = mod
        mod = a % b
    return b

def lcm(a,b):
    return a*b//gcd(a,b)
    
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(nlcm([2,6,8,14]));