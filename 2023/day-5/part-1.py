# --- Day 5: If You Give A Seed A Fertilizer ---
import re


def parse_inputs(file):
    parsed_inputs = {
        "seeds": [],
        "seed_to_soil": { "next": "soil_to_fertilizer" },
        "soil_to_fertilizer": { "next": "fertilizer_to_water" },
        "fertilizer_to_water": { "next": "water_to_light" },
        "water_to_light": { "next": "light_to_temperature" },
        "light_to_temperature": { "next": "temperature_to_humidity" },
        "temperature_to_humidity": { "next": "humidity_to_location" },
        "humidity_to_location": {}
    }
    current_map = {}
    
    for line in file:
        line = line.strip()
        split_line = re.split(" |: ", line)

        if ":" in line:
            if split_line[0] == "seeds":
                parsed_inputs["seeds"].extend(split_line[1:])
            else:
                map_name = split_line[0].replace("-", "_")
                current_map = parsed_inputs[map_name]
                current_map["map"] = []
            
        elif line != "": 
            [dest, src, range_len] = split_line
            current_map["map"].append([int(dest), int(src), int(range_len)])
    
    return parsed_inputs


def get_lowest_location_score(file):
    parsed_inputs = parse_inputs(file)

    # set starting category and map
    current_values = parsed_inputs["seeds"]
    current_map = parsed_inputs["seed_to_soil"]

    while current_map is not None:
        for i in range(len(current_values)):
            item = int(current_values[i])
            for [dest, src, range_len] in current_map["map"]:
                if item >= src and item < src + range_len:
                    current_values[i] = dest + (item - src)
    
        current_map = parsed_inputs[current_map["next"]] if "next" in current_map else None

    return min(current_values)


def main():
    INPUT_FILE = "input.txt"

    with open(INPUT_FILE) as file:
        result = get_lowest_location_score(file)
        print(result)


if __name__ == "__main__":
    main()