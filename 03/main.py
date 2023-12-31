with open("input.txt", "r") as f:
    rows = [line.rstrip() for line in f.readlines()]
num_rows = len(rows)
num_columns = len(rows[0])

# Star 1
def is_symbol(row_index: int, col_index: int):
    current_char = rows[row_index][col_index]
    return (not current_char.isnumeric()) and (current_char != ".")

def check_number_part(row: int, start: int, end: int):
    rows_range = (max(row - 1, 0), min(row + 2, num_rows - 1))
    columns_range = (max(start - 1, 0), min(end + 2, num_columns - 1))
    for r in range(*rows_range):
        for c in range(*columns_range):
            if is_symbol(r, c):
                return True
    return False

def reset_params():
    return "", None

def find_number_parts():
    number_parts = []
    for r in range(len(rows)):
        cursor, start_index = reset_params()
        row = rows[r]
        for c in range(len(row)):
            if row[c].isnumeric():
                if start_index is None:
                    start_index = c
                cursor += str(row[c])
                if c == len(row) - 1:
                    end_index = c
                    if check_number_part(r, start_index, end_index):
                        number_parts.append({"number": int(cursor), "start": start_index, "end": end_index, "row": r})
                    cursor, start_index = reset_params()
            else:
                end_index = c - 1
                if cursor != "":
                    if check_number_part(r, start_index, end_index):
                        number_parts.append({"number": int(cursor), "start": start_index, "end": end_index, "row": r})
                cursor, start_index = reset_params()
    return number_parts

print(sum([obj["number"] for obj in find_number_parts()]))

# Star 2
def find_gears():
    gears = []
    for r in range(len(rows)):
        for c in range(len(rows[r])):
            if rows[r][c] == "*":
                gears.append({"row": r, "column": c})
    return gears

def get_gear_area(row, col):
    row_above = row - 1
    row_below = row + 1
    col_left = col - 1
    col_right = col + 1
    row_range = (max(row_above,0), min(row_below, num_rows - 1) + 1)
    column_range = (max(col_left , 0), min(col_right, num_columns - 1) + 1)
    return (row_range, column_range)

def get_adjacent_number_parts(gear: dict):
    number_parts = []
    area_range = get_gear_area(gear["row"], gear["column"])
    for number_part in find_number_parts():
        if number_part["row"] in range(area_range[0][0], area_range[0][1] + 1):
            for col in range(number_part["start"], number_part["end"] + 1):
                if col in range(area_range[1][0], area_range[1][1] + 1) and number_part not in number_parts:
                    number_parts.append(number_part)
    return number_parts

def calculate_gear_ratio(numbers:int):
    ratio = 1
    for n in numbers:
        ratio *= n
    return ratio

def get_gear_ratio(gear:dict):
    number_parts = get_adjacent_number_parts(gear)
    ratio = 0
    if len(number_parts) > 1:
        return calculate_gear_ratio([obj["number"] for obj in number_parts])
    return ratio

print(sum([get_gear_ratio(gear) for gear in find_gears()]))
