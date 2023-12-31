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
    
    possible_games_sum = 0

    for game_index in range(len(games_list)):
        game_possible = True

        for round in games_list[game_index]:
            for color_count in round:
                number, color = color_count.split()
                number = int(number)

                if (color == "red" and number > 12) or (color == "green" and number > 13) or (color == "blue" and number > 14):
                    game_possible = False
                    break  

            if not game_possible:
                break 

        if game_possible: 
            possible_games_sum += game_index + 1

    print(possible_games_sum)
