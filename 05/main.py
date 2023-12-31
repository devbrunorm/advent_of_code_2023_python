with open("input.txt", "r") as f:
    lines = [line.rstrip() for line in f.readlines()]

def contains_numbers(line: str):
    return any([char.isnumeric() for char in line])

def convert_data():
    data_map = []
    data = {}
    for line_index in range(len(lines)):
        line = lines[line_index]
        if ":" in line:
            if contains_numbers(line):
                data["output"] = line.split(": ")[0][:-1]
                data["values"] = [int(number) for number in line.split(": ")[1].split(" ")]
            else:
                mapping_keys = line.split(" ")[0].split("-to-")
                data["input"] = mapping_keys[0]
                data["output"] = mapping_keys[1]
                data["values"] = []
        elif line != "":
            data["values"].append([int(number) for number in line.split(" ")])
        else:
            data_map.append(data)
            data = {}
    return data_map

def define_mappings():
    converted_data = []
    for data in convert_data():
        if data.get("input") is not None:
            mapping = {}
            for i in range(1000000000):
                mapping[i] = i
            for value in data["values"]:
                k = value[1]
                v = value[0]
                for j in range(value[2]):
                    mapping[k] = v
                    k += 1
                    v += 1
            data["map"] = mapping
        converted_data.append(data)
    return converted_data

data = define_mappings()
locations = []
for seed in data[0]["values"]:
    key = seed
    for mapping_data in data[1:]:
        key = mapping_data["map"][key]
    locations.append(key)

print(min(locations))