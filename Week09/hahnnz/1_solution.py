def N_number(num, N):
    overNum = ['A','B','C','D','E','F']
    if N < 10 or N >10:
        quotient = 0
        remainder = num
        converted = []
        while remainder > N-1:
            quotient = remainder%N
            remainder = remainder//N
            converted.append(quotient)
        converted.append(remainder)
        converted = list(map(str,reversed(converted)))
        if N > 10:
            for i in range(len(converted)):
                if int(converted[i])>9:
                    converted[i]=overNum[int(converted[i][-1])]
        return converted
    
    if N == 10: 
        return list(str(num))
    
def GameGoGo(n,t,m,p):
    answer=[]
    digit=0
    while len(answer)<t*m:        
        answer+=N_number(digit,n)
        digit+=1
    return "".join(answer[p-1:m*t:m])

print(GameGoGo(2,4,2,1))
print(GameGoGo(16,16,2,1))
print(GameGoGo(16,16,2,2))
