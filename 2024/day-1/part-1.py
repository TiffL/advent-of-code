# --- Day 1 ---
import re
import functools


def parse_input(file):
    return [[int(i) for i in re.split(" ", line) if i.strip() != ''] for line in file]


def get_answer(file):
    grid = parse_input(file)

    left = sorted([i for i, j in grid])
    right = sorted([j for i, j in grid])

    return sum([abs(left[i] - right[i]) for i in range(len(left))])


def main():
    INPUT_FILE = "input.txt"

    with open(INPUT_FILE) as file:
        result = get_answer(file)
        print(result)


if __name__ == "__main__":
    main()