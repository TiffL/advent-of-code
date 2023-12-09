# --- Day 9: Mirage Maintenance ---
import re


def get_next_value(sequence):
    latest_sequence = [int(item) for item in sequence]
    total = 0

    while any([item != 0 for item in latest_sequence]):
        total += latest_sequence[0]

        new_sequence = []
        for i, item in enumerate(latest_sequence):
            if i < len(latest_sequence)-1:
                new_sequence.append(item-latest_sequence[i+1])

        latest_sequence = new_sequence

    return total


def main():
    INPUT_FILE = "input.txt"

    with open(INPUT_FILE) as file:
        result = sum([get_next_value(line.strip().split(" ")) for line in file])
        print(result)


if __name__ == "__main__":
    main()