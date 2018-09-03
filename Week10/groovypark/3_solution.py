def solution(n, signs):
    _map = signs
    for y in range(n):
        for x in range(n):
            for z in range(n):
                if _map[x][z] > (_map[x][y] + _map[y][z]):
                    _map[x][z] = _map[x][y] + _map[y][z]

    return _map