# --- Day 2: Cube Conundrum ---
import re


def get_game_score(game, color_to_limits):  
    """
    get_game_score: determines whether a game is possible when played with a given set of cubes

    :param game: string representing a game (several handfuls of cubes retrieved)
    :param color_to_limits: dict representing given set of cubes { color : count }
    :return: game id when game is possible, 0 otherwise
    """

    split_handfuls = re.split(': |; ', game.strip())
    color_to_max_count = {}

    for handful in split_handfuls[1:]:
        split_colors = re.split(',', handful)
        
        for item in split_colors:
            [count, color] = re.split(' ', item.strip())
            if color not in color_to_max_count or int(count) > color_to_max_count[color]:
                color_to_max_count[color] = int(count)
    
    for color in color_to_limits:
        if color in color_to_max_count and color_to_max_count[color] > color_to_limits[color]:
            return 0

    game_id = re.split(' ', split_handfuls[0])[1]

    return int(game_id)


def main():
    INPUT_FILE = "input.txt"
    COLOR_TO_LIMITS = {'red': 12, 'green': 13, 'blue': 14}  # limits set in problem statement
    
    with open(INPUT_FILE) as game_records:
        result = sum([get_game_score(record, COLOR_TO_LIMITS) for record in game_records])
        print(result)


if __name__ == "__main__":
    main()