# --- Day 1: Trebuchet?! ---

def convert_to_num(char):
    if char < '0' or char > '9':
        raise ValueError("Cannot be converted into a number")

    return ord(char) - ord('0')


def get_calibration_value(line):
    digits = []

    for i in range(len(line)):
        if line[i] >= '0' and line[i] <= '9':
            digits.append(line[i])

    if len(digits) == 0:
        raise Exception("Invalid line, no digits found")

    return 10 * convert_to_num(digits[0]) + convert_to_num(digits[len(digits)-1])


def main():
    input_file = "input.txt"
    
    with open(input_file) as calibration_doc:
        result = sum([get_calibration_value(line) for line in calibration_doc])
        print(result)


if __name__ == "__main__":
    main()