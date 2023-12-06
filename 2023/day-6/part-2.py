# --- Day 6: Wait For It ---
import re


def get_ways_to_win(file):
    time = int("".join(re.split("Time:| ", file.readline().strip())))
    distance = int("".join(re.split("Distance:| ", file.readline().strip())))

    return sum([1 for i in range(time) if i*(time-i) > distance])


def main():
    INPUT_FILE = "input.txt"

    with open(INPUT_FILE) as file:
        result = get_ways_to_win(file)
        print(result)


if __name__ == "__main__":
    main()