# --- Day 4 ---
import re
import functools


def parse_input(file):
    return [[i for i in re.split("", line.strip()) if i != ''] for line in file]


def count_word(row, word):
    return count_word_helper(row, word, 1) + count_word_helper(row, word, -1)


def count_word_helper(row, word, direction):
    word = word[::direction]
    count = 0

    i = row.find(word)
    while (i != -1):
        count += 1
        i = row.find(word, i+len(word))

    return count


''' 
realign_diagonals

example, given 3x3: 
0 0 | 0 1 | 0 2
1 0 | 1 1 | 1 2
2 0 | 2 1 | 2 2

expect:
0 0
1 0, 0 1
2 0, 1 1, 0 2
2 1, 1 2
2 2
'''
def realign_diagonals(grid):
    diagonals = []
    for d in range(len(grid)):
        row = []
        j = 0
        for i in range(d, -1, -1):
            if i < len(grid) and j < len(grid[i]):
                row.append(grid[i][j])
            j += 1
        diagonals.append(row)

    for d in range(len(grid[0])-1):
        row = []
        j = d
        for i in range(len(grid), -1, -1):
            if i < len(grid) and j < len(grid[i]):
                row.append(grid[i][j])
            j += 1
        diagonals.append(row)

    return diagonals


def get_answer(file):
    grid = parse_input(file)
    verticals = [[grid[j][i] for j in range(len(grid[0]))] for i in range(len(grid))] # |
    diagonals = realign_diagonals(grid) # /
    diagonals_flipped = realign_diagonals(grid[::-1]) # \

    word = 'XMAS'
    horizontal_count = sum([count_word(''.join(row), word) for row in grid])
    vertical_count = sum([count_word(''.join(row), word) for row in verticals])
    diagonal_count = sum([count_word(''.join(row), word) for row in diagonals])
    diagonal_count += sum([count_word(''.join(row), word) for row in diagonals_flipped])

    return horizontal_count + vertical_count + diagonal_count


def main():
    INPUT_FILE = "input.txt"

    with open(INPUT_FILE) as file:
        result = get_answer(file)
        print(result)


if __name__ == "__main__":
    main()