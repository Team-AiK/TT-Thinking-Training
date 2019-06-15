import collections
def solution(B):
    position = {
        "x": 0,
        "y": 0,
        "l": 0
    }

    if not B or not B[0]:
        return 0

    up_left = (-1, -1)
    up_right = (-1, 1)

    for y in range(len(B)):
        for x in range(len(B[y])):
            if B[y][x] == "O":
                position["x"], position["y"] = x, y
                break
                
    q = collections.deque()
    q.append(position)

    ans = 0
    while q:
        cur = q.popleft()
        ans = max(ans, cur["l"])
        for dy, dx in [up_left, up_right]:
            ny, nx = cur["y"]+dy, cur["x"]+dx
            if ny < 0 or nx < 0 or ny >= len(B) or nx >= len(B[0]):
                continue
            if B[ny][nx] != "X":
                continue
            oy, ox = ny + dy, nx + dx
            if oy < 0 or ox < 0 or oy >= len(B) or ox >= len(B[0]):
                continue
            if B[oy][ox] == "X":
                continue
            q.append({
                "x": ox,
                "y": oy,
                "l": cur["l"]+1
            })

    return ans

B = ["..X...", ".....", "....X.", ".X....", "..X.X.", "...O.."]
print(solution(B))
