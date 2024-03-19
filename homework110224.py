def coord(point: str) -> tuple:
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

print(coord("SNNNWEESENSWWWW"))

#1.1
def get_coordinates(movement_arr: str) -> tuple:
    x_coord = movement_arr.count("E") - movement_arr.count("W")
    y_coord = movement_arr.count("N") - movement_arr.count("S")
    return x_coord, y_coord

#1.2
def get_coordinates(movement_arr: str, start_coord: tuple) -> tuple:
    if not isinstance(movement_arr, str):
        return ValueError
    if not movement_arr.isalpha():
        return ValueError
    if len(start_coord) != 2:
        return ValueError

    x_coord, y_coord = start_coord[0], start_coord[1]
    if not (isinstance(x_coord, int) or isinstance(y_coord, int)):
        return ValueError
    x_coord = movement_arr.count("E") - movement_arr.count("W")
    y_coord = movement_arr.count("N") - movement_arr.count("S")
    return x_coord, y_coord

#1.3
def get_coordinates(movement_arr: str, start_coord: tuple) -> tuple:
    if not isinstance(movement_arr, str):
        return ValueError
    if not movement_arr.isalpha():
        return ValueError
    if len(start_coord) != 2:
        return ValueError
    x_coord, y_coord = start_coord[0], start_coord[1]
    if not (isinstance(x_coord, int) or isinstance(y_coord, int)):
        return ValueError
    if  x_coord not in range(0, 101) or y_coord not in range(0, 101):
        return ValueError("Not correct start coord")
    for m in movement_arr:
        if m == "E":
            x_coord += 1
        elif m == "W":
            x_coord -= 1
        elif m == "N":
            y_coord += 1
        else:
            y_coord -= 1
        if x_coord not in range(0, 101) or y_coord not in range(0, 101):
            return start_coord

    return x_coord, y_coord