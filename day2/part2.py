import re

def set_number(text):
    games = re.split(r"Game \d+: ", text)

    if games[0] == '':
        games.pop(0)

    games_list = []
    for game in games:
        game_parts = [part.strip().split(", ") for part in game.split(";")]
        games_list.append(game_parts)
    return games_list


with open("input.txt", "r") as file:
    data = file.read()
    games_list = set_number(data)
    
    max_red = 0
    max_green = 0
    max_blue = 0
    
    power = 0
    for game_index in range(len(games_list)):
        for round in games_list[game_index]:
            for color_count in round:
                number, color = color_count.split()
                number = int(number)

                if color == "red" and number > max_red:
                    max_red = number
                elif color == "green" and number > max_green:
                    max_green = number
                elif color == "blue" and number > max_blue:
                    max_blue = number
        power += max_red * max_green * max_blue
        max_red = 0
        max_green = 0
        max_blue = 0
            

    print(power)
   
