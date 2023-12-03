# --- Day 2: Cube Conundrum ---
import re


def get_game_power(game):
    """
    get_game_power: determines the "power" of a game

    :param game: string representing a game (several handfuls of cubes retrieved)
    :return: the "power" of a game, as defined equal to the numbers of red, green, 
             and blue cubes multiplied together
    """

    POWER_COLORS = ['red', 'green', 'blue']

    split_handfuls = re.split(': |; ', game.strip())
    color_to_max_count = {}

    for handful in split_handfuls[1:]:
        split_colors = re.split(',', handful)
        
        for item in split_colors:
            [count, color] = re.split(' ', item.strip())
            if color not in color_to_max_count or int(count) > color_to_max_count[color]:
                color_to_max_count[color] = int(count)
    
    power = 1
    for color in POWER_COLORS:
        if color not in color_to_max_count:
            return 0
        
        power *= color_to_max_count[color]

    return power


def main():
    INPUT_FILE = "input.txt"
    
    with open(INPUT_FILE) as game_records:
        result = sum([get_game_power(record) for record in game_records])
        print(result)


if __name__ == "__main__":
    main()