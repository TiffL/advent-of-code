# --- Day 10: Pipe Maze ---
import re


def parse_input(file):
    return [[i for i in re.split("", line.strip()) if i != ''] for line in file]


def get_starting_point(diagram):
    START_TILE = 'S'
    CHECK_NEXT = [
        {"movement": [-1, 0], "possibilities": '|7F'},
        {"movement": [ 1, 0], "possibilities": '|JL'},
        {"movement": [ 0,-1], "possibilities": '-LF'},
        {"movement": [ 0, 1], "possibilities": '-J7'}
    ]
    
    num_rows = len(diagram)
    num_cols = len(diagram[0]) if num_rows > 0 else 0

    start_r = 0
    start_c = 0
    next_r = -1
    next_c = -1

    for r in range(len(diagram)):
        for c in range(len(diagram[0])):
            if diagram[r][c] == START_TILE:
                start_r = r
                start_c = c
                break

    for check in CHECK_NEXT:
        [dr, dc] = check["movement"]
        next_r = start_r + dr
        next_c = start_c + dc

        if next_r >= 0 and next_r < num_rows and \
            next_c >= 0 and next_c < num_cols and \
            diagram[next_r][next_c] in check["possibilities"]:
            break

    return start_r, start_c, next_r, next_c


def move_through_pipe(diagram, i, j, prev_i, prev_j):
    PIPES = { # origin to movement
	    '|': {'N': [1, 0], 'S': [-1, 0]},
        '-': {'W': [0, 1], 'E': [ 0,-1]},
        'L': {'N': [0, 1], 'E': [-1, 0]},
        'J': {'N': [0,-1], 'W': [-1, 0]},
        '7': {'W': [1, 0], 'S': [ 0,-1]},
        'F': {'E': [1, 0], 'S': [ 0, 1]}
    }

    origin = 'N' if i > prev_i else 'S'
    if j != prev_j:
        origin = 'W' if j > prev_j else 'E'

    tile = diagram[i][j]
    new_r = i+PIPES[tile][origin][0]
    new_c = j+PIPES[tile][origin][1]

    return new_r, new_c


def get_answer(file):
    diagram = parse_input(file)
    start_r, start_c, r, c = get_starting_point(diagram)
    prev_r = start_r
    prev_c = start_c
    steps = 1
    
    while not (r == start_r and c == start_c):
        steps += 1
        new_r, new_c = move_through_pipe(diagram, r, c, prev_r, prev_c)
        prev_r = r
        prev_c = c
        r = new_r
        c = new_c

    return int(steps / 2)


def main():
    INPUT_FILE = "input.txt"

    with open(INPUT_FILE) as file:
        result = get_answer(file)
        print(result)


if __name__ == "__main__":
    main()