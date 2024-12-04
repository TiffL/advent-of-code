# --- Day 3 ---
import re
import functools


def parse_input(file):
    return ''.join(file)


def get_answer(file):
    INDICATOR_START = 'mul('
    INDICATOR_END = ')'
    
    puzzle = parse_input(file)
    res = 0

    i = puzzle.find(INDICATOR_START)
    while (i != -1):
        start = i+len(INDICATOR_START)
        try:
            # attempt to parse corrupted "memory"
            a, b = puzzle[start:puzzle.find(INDICATOR_END, i)].split(',')
            res += int(a) * int(b)
        except:
            # skip over corrupted portions
            pass
        
        i = puzzle.find(INDICATOR_START, start)

    return res


def main():
    INPUT_FILE = "input.txt"

    with open(INPUT_FILE) as file:
        result = get_answer(file)
        print(result)


if __name__ == "__main__":
    main()