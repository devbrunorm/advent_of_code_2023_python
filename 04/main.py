with open("input.txt", "r") as f:
    lines = [line.rstrip() for line in f.readlines()]

def calculate_point(matches):
    if len(matches) > 0:
        return 2**(len(matches) - 1)
    return 0
    

def get_card_data(line_str):
    data = line_str.split(": ")
    card_id = int(data[0].split(" ")[-1])
    number_str = data[1].split(" | ")
    winning_nums = [int(num) for num in number_str[0].split(" ") if num != ""]
    own_nums = [int(num) for num in number_str[1].split(" ") if num != ""]
    matches = list(set(winning_nums).intersection(set(own_nums)))
    return {
        "id": card_id,
        "winning": winning_nums,
        "own": own_nums,
        "matches": matches,
        "points": calculate_point(matches),
        "copies": 1
    }

def concat_data():
    data = {}
    for line in lines:
        card_data = get_card_data(line)
        data[card_data["id"]] = card_data
    return data

global_data = concat_data()

# Star 1
points = 0
for id, data in global_data.items():
    points += data["points"]
print(points)

# Star 2
for id, data in global_data.items():
    matches = len(data["matches"])
    if matches > 0:
        for copy in range(data["copies"]):
            for i in range(id + 1, id + matches + 1):
                new_data = global_data[i]
                new_data["copies"] += 1
                global_data[i] = new_data
print(sum([global_data[key]["copies"] for key in global_data.keys()]))