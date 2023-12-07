# --- Day 7: Camel Cards ---
import re
import functools


def parse_input(file):
    result = []
    for line in file:
        [hand, bid] = re.split("\s+", line.strip())
        result.append({
            "hand": hand,
            "bid": int(bid),
            "type": get_hand_type(hand)
        })
    
    return result


def get_hand_type(hand):
    HAND_TYPE_REQS = {
        "5": 7,         # five of a kind, represented by 7
        "4,1": 6,       # four of a kind, represented by 6
        "3,2": 5,       # full house
        "3,1,1": 4,     # three of a kind
        "2,2,1": 3,     # two pair
        "2,1,1,1": 2,   # one pair
        "1,1,1,1,1": 1  # high card
    }
    WILDCARD = 'J'

    wildcard_count = 0
    card_counts = {}
    for card in hand:
        if card == WILDCARD:
            wildcard_count += 1
            continue 

        if card not in card_counts:
            card_counts[card] = 0

        card_counts[card] += 1
    
    hand_type = 0
    if wildcard_count == 5:  # all jokers
        hand_type = HAND_TYPE_REQS["5"]
    else:
        sorted_hand = [str(count) for card, count in sorted(card_counts.items(), key=lambda x: x[1], reverse=True)]
        sorted_hand[0] = str(int(sorted_hand[0]) + wildcard_count)
        hand_representation = ",".join(sorted_hand)
        hand_type = HAND_TYPE_REQS[hand_representation]
    
    return hand_type


def hand_comparator(h1, h2):
    if h1["type"] != h2["type"]:
        return h1["type"] - h2["type"]

    CARD_RANKING = {'A':13, 'K':12, 'Q':11, 'T':10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2, 'J': 1}
    
    for (c1, c2) in zip(h1["hand"], h2["hand"]):
        if c1 != c2:
            return CARD_RANKING[c1] - CARD_RANKING[c2]
    
    return 0


def get_total_winnings(file):
    hands = parse_input(file)
    sorted_hands = sorted(hands, key=functools.cmp_to_key(hand_comparator))

    return sum([hand["bid"]*(i+1) for i, hand in enumerate(sorted_hands)])


def main():
    INPUT_FILE = "input.txt"

    with open(INPUT_FILE) as file:
        result = get_total_winnings(file)
        print(result)


if __name__ == "__main__":
    main()