def coord(point: str) -> tuple:
    if not set(point) <= {'S', 'N', 'W', 'E'}:
        return ValueError ("Введите координаты S, N, W или E")
    x = 0
    y = 0
    for value in point:
        if value == "S":
            y -= 1
        elif value == "N":
            y += 1
        elif value == "W":
            x -= 1
        elif value == "E":
            x += 1
    res_point = (x, y)
    return res_point

print(coord("Z"))