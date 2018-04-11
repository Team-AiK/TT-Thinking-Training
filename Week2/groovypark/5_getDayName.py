def getDayName(a,b):
    dayName = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    days = [31,29,31,30,31,30,31,31,30,31,30,31]
    sumDay = 0
    for day in days[0:a-1]:
        sumDay = sumDay + day
    answer = dayName[(sumDay+b)%7]

    return answer

#아래 코드는 테스트를 위한 출력 코드입니다.
print(getDayName(5,24))