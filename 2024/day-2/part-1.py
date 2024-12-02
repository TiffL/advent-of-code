# --- Day 2 ---
import re
import functools


def parse_input(file):
    return [[int(i) for i in re.split(" ", line) if i.strip() != ''] for line in file]


def is_safe(report):
    deltas = [report[i] - report[i-1] for i in range(len(report)) if i > 0]
    initial_sign = deltas[0] > 0

    has_same_sign = all([True if (delta > 0 and initial_sign) or (delta < 0 and not initial_sign) else False for delta in deltas])
    is_within_range = all([True if abs(delta) >= 1 and abs(delta) <= 3 else False for delta in deltas])

    return has_same_sign and is_within_range


def get_answer(file):
    reports = parse_input(file)

    return sum([1 for report in reports if is_safe(report)])


def main():
    INPUT_FILE = "input.txt"

    with open(INPUT_FILE) as file:
        result = get_answer(file)
        print(result)


if __name__ == "__main__":
    main()