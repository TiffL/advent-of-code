import re
import math


def get_gear_id(i, j):
    return f"{i}|{j}"


def is_digit(char):
    return char >= '0' and char <= '9'


def get_all_gear_locations(schematic):
    res = {}

    for i, line in enumerate(schematic):
        line = line.strip()
        for j, item in enumerate(line):
            if item == '*':
                res[get_gear_id(i, j)] = True

    return res


def get_adjacent_gears(i, j, symbol_locations):
    rows = [i-1, i, i+1]
    cols = [j-1, j, j+1]

    return [get_gear_id(r, c) for c in cols for r in rows if get_gear_id(r, c) in symbol_locations]


def get_gear_ratio(schematic, symbol_locations):
    gear_to_ratio = {}

    for i, line in enumerate(schematic):
        line = line.strip()

        number = ""
        is_adjacent = False
        adjacent_gears = {}

        for j, char in enumerate(line):
            if is_digit(char):
                char_adjacent = get_adjacent_gears(i, j, symbol_locations)

                for gear_id in char_adjacent:
                    if gear_id not in adjacent_gears:
                        adjacent_gears[gear_id] = True

                is_adjacent = is_adjacent or len(char_adjacent) > 0
                number += char
            
            if not is_digit(char) or j == len(line)-1:
                if number != "" and is_adjacent:
                    for gear_id in adjacent_gears:
                        if gear_id not in gear_to_ratio:
                            gear_to_ratio[gear_id] = []
                        
                        gear_to_ratio[gear_id].append(int(number))

                number = ""
                is_adjacent = False
                adjacent_gears = {}

    return sum([math.prod(ratios) for ratios in gear_to_ratio.values() if len(ratios) > 1])


def main():
    INPUT_FILE = "input.txt"
    symbol_locations = {}
    
    with open(INPUT_FILE) as schematic:
        symbol_locations = get_all_gear_locations(schematic)

    with open(INPUT_FILE) as schematic:
        result = get_gear_ratio(schematic, symbol_locations)
        print(result)


if __name__ == "__main__":
    main()