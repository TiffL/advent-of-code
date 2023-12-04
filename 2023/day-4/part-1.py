#--- Day 4: Scratchcards ---
import re

def get_match_scores(line):
    _, winning_nums, card = re.split(': | \| ', line.strip())
    winning_nums = { num for num in re.split(' ', winning_nums) }
    card = re.split(' ', card)

    total = 0
    for num in card:
        if num != '' and num in winning_nums:
            total = 1 if total == 0 else total * 2

    return total


def main():
    INPUT_FILE = "input.txt"
    symbol_locations = {}

    with open(INPUT_FILE) as file:
        result = sum([get_match_scores(line) for line in file])
        print(result)


if __name__ == "__main__":
    main()