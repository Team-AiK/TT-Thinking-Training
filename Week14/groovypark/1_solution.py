def solution(participant, completion):
    dic = {}
    for person in participant:
        dic[person] = 0
    for person in participant:
        dic[person] += 1
    for person in completion:
        dic[person] -= 1
    for person in dic:
        if dic[person] == 1:
            return person

print(solution(	["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))