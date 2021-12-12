from typing import Dict, List, Set


def read_input(file_path: str) -> List[str]:
    with open(file_path) as f:
        file_content = f.read().splitlines()
        return file_content


class Node:
    def __init__(self, name: str) -> None:
        self.neighbours: List[Node] = []
        self.name = name
        self.size = "big" if name.upper() == name else "small"


def main(data: List[str], multi_visit_small: bool = False):
    nodes: Dict[str, Node] = dict()

    for line in data:
        from_node, to_node = line.split("-")
        if not from_node in nodes.keys():
            nodes[from_node] = Node(from_node)
        if not to_node in nodes.keys():
            nodes[to_node] = Node(to_node)
        nodes[from_node].neighbours.append(nodes[to_node])
        nodes[to_node].neighbours.append(nodes[from_node])

    visited = []
    paths = traverse(nodes, visited.copy(), nodes["start"], not multi_visit_small)
    print(len(paths))


def traverse(nodes: Dict[str, Node], visited: List[Node], current: Node, has_visited_small_twice: bool) -> Set[str]:
    paths = set()
    if current.name == "end":
        paths.add(",".join(map(lambda n: n.name, visited)))
        return paths

    for n in current.neighbours:
        if (n.name != "start") and ((not n in visited) or (n.size == "big") or (not has_visited_small_twice)):
            paths.update(traverse(nodes, visited.copy() + [n], n,
                                  has_visited_small_twice or ((n in visited) and n.size == "small")))
    return paths


if __name__ == "__main__":
    # Task 1
    file_content = read_input("src/12/data.txt")
    main(file_content)
    # Task 2
    main(file_content, multi_visit_small=True)
