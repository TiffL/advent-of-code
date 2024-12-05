# --- Day 4 ---
import re
import functools


def parse_input(file):
    return [[i for i in re.split("", line.strip()) if i != ''] for line in file]


def is_xmas(grid):
    relevant = [grid[0][0], grid[0][2], grid[2][0], grid[2][2]]

    num_m = sum([1 for item in relevant if item == 'M'])
    num_s = sum([1 for item in relevant if item == 'S'])

    has_valid_pairings = \
        (grid[0][0] == 'M' and grid[2][2] == 'S') or \
        (grid[0][0] == 'S' and grid[2][2] == 'M') or \
        (grid[0][2] == 'M' and grid[2][0] == 'S') or \
        (grid[0][2] == 'S' and grid[2][0] == 'M')
    
    return num_m == 2 and num_s == 2 and has_valid_pairings


def get_answer(file):
    grid = parse_input(file)
    count = 0
    
    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[0])-1):
            if grid[i][j] == 'A' and is_xmas([row[j-1:j+2] for row in grid[i-1:i+2]]):
                count += 1

    return count


def main():
    INPUT_FILE = "input.txt"

    with open(INPUT_FILE) as file:
        result = get_answer(file)
        print(result)


if __name__ == "__main__":
    main()