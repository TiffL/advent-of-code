# --- Day 1 ---
import re
import functools


def parse_input(file):
    return [[int(i) for i in re.split(" ", line) if i.strip() != ''] for line in file]


def get_answer(file):
    grid = parse_input(file)

    left = sorted([i for i, j in grid])
    right = sorted([j for i, j in grid])
    
    count = {}
    for item in right: 
        if item not in count: 
            count[item] = 0
        count[item] += 1

    return sum([item * count[item] for item in left if item in count])


def main():
    INPUT_FILE = "input.txt"

    with open(INPUT_FILE) as file:
        result = get_answer(file)
        print(result)


if __name__ == "__main__":
    main()