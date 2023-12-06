# --- Day 6: Wait For It ---
import re


def parse_inputs(file):
    times = [int(item) for item in re.split("Time:| ", file.readline().strip()) if item != ""]
    distances = [int(item) for item in re.split("Distance:| ", file.readline().strip()) if item != ""]
    return times, distances


def get_ways_to_win(file):
    times, distances = parse_inputs(file)

    result = 1
    for time, distance in zip(times, distances):
        result *= sum([1 for i in range(time) if i*(time-i) > distance])

    return result


def main():
    INPUT_FILE = "input.txt"

    with open(INPUT_FILE) as file:
        result = get_ways_to_win(file)
        print(result)


if __name__ == "__main__":
    main()