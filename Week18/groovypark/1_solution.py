def solution(ranks):
    set_ranks = set(ranks)
    soldier = 0
    for r in ranks:
        if r+1 in set_ranks:
            soldier += 1
    return soldier
