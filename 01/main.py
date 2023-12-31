NUMBERS_NAMES = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0",
}

def get_first_last_number(line: str, include_string: bool = False):
    first = None
    last = None
    for char_index in range(len(line)):
        substring = line[char_index:]
        current_char = line[char_index]
        if current_char.isnumeric():
            last = current_char
        elif include_string:
            for number_name, number in NUMBERS_NAMES.items():
                if substring.startswith(number_name):
                    last = number
        if first is None:
            first = last
    return first, last

def generate_code_line(line, include_string = False):
    first, last = get_first_last_number(line, include_string)
    return int(first+last)

with open("input.txt", "r") as f:
    lines = f.readlines()

# Star 1
    print(sum([generate_code_line(line) for line in lines]))

# Star 2
    print(sum([generate_code_line(line, include_string = True) for line in lines]))
