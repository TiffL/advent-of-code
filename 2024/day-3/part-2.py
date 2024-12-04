# --- Day 3 --- not pretty but it works
import re
import functools


def parse_input(file):
    return ''.join(file)


def parse_do_donts(puzzle):
    process_spans = []

    is_instruction_enabled = True
    i = 0

    while i != -1 and i < len(puzzle):
        search_phrase = "don't()" if is_instruction_enabled else "do()"

        if is_instruction_enabled:
            end = puzzle.find(search_phrase, i+1)
            process_spans.append((i, len(puzzle) if end == -1 else end))
            i = end
        else:
            i = puzzle.find(search_phrase, i+1)
        
        is_instruction_enabled = not is_instruction_enabled

    return process_spans


def get_answer(file):
    INDICATOR_START = 'mul('
    INDICATOR_END = ')'
    res = 0
    
    puzzle = parse_input(file)
    process_spans = parse_do_donts(puzzle)

    for (span_start, span_end) in process_spans:
        segment = puzzle[span_start:span_end]

        i = segment.find(INDICATOR_START)
        while (i != -1):
            start = i+len(INDICATOR_START)
            try:
                # attempt to parse corrupted "memory"
                a, b = segment[start:segment.find(INDICATOR_END, i)].split(',')
                res += int(a) * int(b)
            except:
                # skip over corrupted portions
                pass
            
            i = segment.find(INDICATOR_START, start)
        
    return res


def main():
    INPUT_FILE = "input.txt"

    with open(INPUT_FILE) as file:
        result = get_answer(file)
        print(result)


if __name__ == "__main__":
    main()