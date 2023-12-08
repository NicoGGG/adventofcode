def resolve_exercise(filepath: str):
    file = open(filepath, "r")
    lines = file.read().splitlines()
    file.close()
    directions = lines[0]
    network = lines[2:]
    network_dict: dict[dict[str:str]] = {}
    for line in network:
        node = line.split("=")[0].strip()
        node_dict = {
            "left": line.split("=")[1].strip().strip("()").split(",")[0].strip(),
            "right": line.split("=")[1].strip().strip("()").split(",")[1].strip(),
        }
        network_dict[node] = node_dict
    starting_node_str = network[0].split("=")[0].strip()
    current_node = network_dict[starting_node_str]
    r = 0
    l = len(directions)
    while True:
        direction_index = r % l
        next_direction = directions[direction_index]
        if next_direction == "L":
            next_node_str = current_node["left"]
        else:
            next_node_str = current_node["right"]
        current_node: dict = network_dict[next_node_str]
        r += 1
        if next_node_str == "ZZZ":
            return r
