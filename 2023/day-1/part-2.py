# --- Day 1: Trebuchet?! ---

def get_calibration_value(line):
    digits_text_to_value = {
        "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
        "zero": 0, "one": 1, "two": 2, "three": 3, "four" : 4, "five": 5,
        "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9
    }

    first_digit = -1
    second_digit = -1
    first_digit_i = len(line)  # start index of first digit
    last_digit_i = -1          # start index of last digit

    for key in digits_text_to_value.keys():
        if key not in line:
            continue

        first_occurrence = line.index(key)
        last_occurrence = line.rindex(key)

        if first_occurrence < first_digit_i:
            first_digit = digits_text_to_value[key]
            first_digit_i = first_occurrence
        
        if last_occurrence > last_digit_i:
            second_digit = digits_text_to_value[key]
            last_digit_i = last_occurrence


    if first_digit == -1 and last_digit == -1:
        raise Exception("Invalid line, no digits found")
    elif first_digit == -1:
        first_digit = second_digit
    elif second_digit == -1:
        second_digit = first_digit

    return 10 * first_digit + second_digit


def main():
    input_file = "input.txt"
    
    with open(input_file) as calibration_doc:
        result = sum([get_calibration_value(line) for line in calibration_doc])
        print(result)


if __name__ == "__main__":
    main()