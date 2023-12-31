def get_game_id(game: str) -> int:
    game_id = game.split(":")[0]
    return int(game_id.split(" ")[-1])

def obtain_color_count(information_count: dict, color:str) -> int:
    return information_count.get(color) or 0

def format_color_info(information_dict: dict) -> tuple:
    return (
        obtain_color_count(information_dict, "red"), 
        obtain_color_count(information_dict, "green"),  
        obtain_color_count(information_dict, "blue")
    )

def get_color_information(information_str: str) -> tuple:
    information = {}
    for information_color in information_str.split(", "):
        information_color_list = information_color.split(" ")
        number = int(information_color_list[0])
        color = information_color_list[1]
        information[color] = number
    return format_color_info(information)

def get_game_information(game: str) -> list:
    game_informations_str = game.split(": ")[-1].replace("\n", "")
    return [get_color_information(information_str) for information_str in game_informations_str.split("; ")]

def is_possible_game(game, preset) -> bool:
    for info in game:
        for i in range(3):
            if int(info[i]) > preset[i]:
                return False
    return True

def get_max_color_values(info_list: list):
    max_counts = {}
    max_counts["red"] = max([count[0] for count in info_list])
    max_counts["green"] = max([count[1] for count in info_list])
    max_counts["blue"] = max([count[2] for count in info_list])
    return format_color_info(max_counts)

# Star 1
possible_games_ids = []
with open("input.txt", "r") as f:
    for game in f.readlines():
        game_information = get_game_information(game)
        if is_possible_game(game_information, (12, 13, 14)):
            possible_games_ids.append(get_game_id(game))
print(sum(possible_games_ids))

# Star 2
power_games = []
with open("input.txt", "r") as f:
    for game in f.readlines():
        game_information = get_game_information(game)
        max_values = get_max_color_values(game_information)
        power_games.append(max_values[0]*max_values[1]*max_values[2])
print(sum(power_games))