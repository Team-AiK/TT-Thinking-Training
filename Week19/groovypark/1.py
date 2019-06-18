def solution(s):
    p = 0
    y = 0
    
    for ss in s:
        if ss == 'p' or ss == 'P':
            p += 1
        elif ss == 'y' or ss == 'Y':
            y += 1
    if p == y:
        return True
    return False