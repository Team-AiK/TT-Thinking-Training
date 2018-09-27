def solution2(msg):
    dictionary = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    answer = []
    while len(msg) != 0:
        if msg in dictionary:
            answer.append(dictionary.index(msg)+1)
            return answer
        for i in range(1,len(msg)+1):
            if msg[0:i] in dictionary:
                pass
            else:
                dictionary.append(msg[0:i])
                index = dictionary.index(msg[0:i-1])
                answer.append(index+1)
                msg = msg[i-1:]
                break


print(solution2('ABABABABABABABAB'))
