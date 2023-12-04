#--- Day 4: Scratchcards ---
import re

def get_match_scores(file):
    total = 0
    card_to_multiplier = {}

    for i, line in enumerate(file):
        _, winning_nums, card = re.split(': | \| ', line.strip())
        winning_nums = { num for num in re.split(' ', winning_nums) }
        card = re.split(' ', card)
        
        num_matches = 0
        for num in card:
            if num != '' and num in winning_nums:
                num_matches += 1

        total_card_i = card_to_multiplier[i] if i in card_to_multiplier else 1
        
        if num_matches > 0:
            for j in range(i+1, i+num_matches+1):
                if j not in card_to_multiplier:
                    card_to_multiplier[j] = 1

                card_to_multiplier[j] += total_card_i

        total += total_card_i

    return total


def main():
    INPUT_FILE = "input.txt"
    symbol_locations = {}

    with open(INPUT_FILE) as file:
        result = get_match_scores(file)
        print(result)


if __name__ == "__main__":
    main()