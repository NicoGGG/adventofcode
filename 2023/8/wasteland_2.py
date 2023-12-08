import math


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
    starting_nodes_str: list[str] = [
        key for key in filter(lambda key: key.endswith("A"), network_dict)
    ]
    current_nodes = [network_dict[node] for node in starting_nodes_str]
    r = 0
    rs = [0 for x in current_nodes]
    l = len(directions)
    while True:
        direction_index = r % l
        next_direction = directions[direction_index]
        next_nodes_str: list[str] = []
        for i, current_node in enumerate(current_nodes):
            if next_direction == "L":
                next_node_str = current_node["left"]
            else:
                next_node_str = current_node["right"]
            next_nodes_str.append(next_node_str)
            current_nodes[i] = network_dict[next_node_str]
        r += 1
        for i, current_node in enumerate(current_nodes):
            if next_nodes_str[i].endswith("Z"):
                rs[i] = r
        if all(r != 0 for r in rs):
            break

    return math.lcm(*rs)
