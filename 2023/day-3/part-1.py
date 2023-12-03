import re


def get_symbol_id(i, j):
    return f"{i}|{j}"


def is_digit(char):
    return char >= '0' and char <= '9'


def get_all_symbol_locations(schematic):
    res = {}

    for i, line in enumerate(schematic):
        line = line.strip()
        for j, char in enumerate(line):
            if char != '.' and not is_digit(char):
                res[get_symbol_id(i, j)] = True

    return res


def has_adjacent_symbol(i, j, symbol_locations):
    rows = [i-1, i, i+1]
    cols = [j-1, j, j+1]

    for r in rows:
        for c in cols:
            if get_symbol_id(r, c) in symbol_locations:
                return True
    
    return False


def get_part_number(schematic, symbol_locations):
    total = 0

    for i, line in enumerate(schematic):
        line = line.strip()
        number = ""
        is_part = False

        for j, char in enumerate(line):
            if is_digit(char):
                is_part = is_part or has_adjacent_symbol(i, j, symbol_locations)
                number += char
            
            if not is_digit(char) or j == len(line)-1:
                if number != "" and is_part:
                    total += int(number)

                number = ""
                is_part = False

    return total


def main():
    INPUT_FILE = "input.txt"
    symbol_locations = {}
    
    with open(INPUT_FILE) as schematic:
        symbol_locations = get_all_symbol_locations(schematic)

    with open(INPUT_FILE) as schematic:
        result = get_part_number(schematic, symbol_locations)
        print(result)


if __name__ == "__main__":
    main()