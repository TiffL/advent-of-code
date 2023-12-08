# --- Day 8: Haunted Wasteland ---
import re


def parse_input(file):
    instructions = [i for i in re.split("", file.readline().strip()) if i != '']
    network_connections = {}

    for line in file:
        line = line.strip()
        if line == "":
            continue
        
        [start_node, end_nodes] = re.split(" = ", line)
        network_connections[start_node] = re.split(", ", end_nodes[1:len(end_nodes)-1])

    return instructions, network_connections


def get_answer(file):
    START_NODE = 'AAA'
    DESTINATION_NODE = 'ZZZ'

    instructions, network_connections = parse_input(file)
    
    if len(instructions) == 0 or len(network_connections) == 0:
        return -1

    found = False
    steps = 0
    instruction_i = 0
    current_node = START_NODE

    while current_node != DESTINATION_NODE:
        steps += 1
        is_right = instructions[instruction_i] == 'R'
        current_node = network_connections[current_node][is_right]
        instruction_i = instruction_i+1 if instruction_i < len(instructions)-1 else 0

    return steps


def main():
    INPUT_FILE = "input.txt"

    with open(INPUT_FILE) as file:
        result = get_answer(file)
        print(result)


if __name__ == "__main__":
    main()