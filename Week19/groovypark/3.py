def solution(s):
    s = s.lower()
    L=s.split(" ")
    answer = ""
    for i in L:
        i= i.capitalize()
        answer+= i+" "
    return answer[:-1]

# 무슨 차이지? 21.9점
# def solution(s):
#     answer = ''
#     s = s.lower()
#     arr = s.split()
#     for word in arr:
#         answer += word.capitalize() + " "
#     return answer[:-1]
