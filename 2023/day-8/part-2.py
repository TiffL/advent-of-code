# --- Day 8: Haunted Wasteland ---
import re
import numpy as np


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
    instructions, network_connections = parse_input(file)
    starting_points = [node for node in network_connections if node[len(node)-1] == 'A']
    
    if len(instructions) == 0 or len(network_connections) == 0:
        return -1

    current_steps = 0
    instruction_i = 0
    current_nodes = starting_points
    stopping_steps = []

    while len(current_nodes) > 0:
        current_steps += 1
        is_right = instructions[instruction_i] == 'R'
        current_nodes = [network_connections[current_node][is_right] for current_node in current_nodes]
        instruction_i = instruction_i+1 if instruction_i < len(instructions)-1 else 0

        new_nodes = []

        for node in current_nodes:
            if node[len(node)-1] == 'Z':
                stopping_steps.append(current_steps)
            else:
                new_nodes.append(node)

        current_nodes = new_nodes

    return np.lcm.reduce(stopping_steps)


def main():
    INPUT_FILE = "input.txt"

    with open(INPUT_FILE) as file:
        result = get_answer(file)
        print(result)


if __name__ == "__main__":
    main()