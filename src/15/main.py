from typing import List
import numpy as np
from sys import maxsize
from itertools import chain
import heapq


def read_input(file_path: str) -> List[str]:
    with open(file_path) as f:
        file_content = f.read().splitlines()
        return file_content


class Node:
    def __init__(self, name: str, risk: int) -> None:
        self.name = name
        self.risk = risk
        self.neighbours: List[Node] = []
        self.total = maxsize

    def __lt__(self, other):
        return self.total < other.total


def dijkstra(graph: List[Node], start: Node):
    start.total = 0
    queue = []
    for node in graph:
        heapq.heappush(queue, node)
    while len(queue) > 0:
        current_node = heapq.heappop(queue)
        for neighbour in current_node.neighbours:
            if neighbour.total > current_node.total + neighbour.risk:
                neighbour.total = current_node.total + neighbour.risk
                heapq.heapify(queue)


def main(data: List[str], larger=False):
    matrix = np.array([[int(c) for c in row] for row in data], dtype=np.int8)
    if larger:
        n, m = len(matrix), len(matrix[0])
        matrix = np.array([[matrix[y % n, x % m] + y//n + x//m for x in range(m*5)]
                           for y in range(n*5)], dtype=np.int8)
        matrix[matrix > 9] -= 9

    graph: List[List[Node]] = [[Node(f"{y}{x}", matrix[y, x])
                                for x in range(len(matrix[0]))] for y in range(len(matrix))]
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            node = graph[y][x]
            if y > 0:
                node.neighbours.append(graph[y-1][x])
            if y < len(matrix) - 1:
                node.neighbours.append(graph[y+1][x])
            if x > 0:
                node.neighbours.append(graph[y][x-1])
            if x < len(matrix[0]) - 1:
                node.neighbours.append(graph[y][x+1])

    start, end = graph[0][0], graph[-1][-1]
    flat_graph = list(chain.from_iterable(graph))
    dijkstra(flat_graph, start)
    print(end.total)


if __name__ == "__main__":
    # Task 1
    file_content = read_input("src/15/data.txt")
    main(file_content)
    # Task 2
    main(file_content, larger=True)  # Takes approx 2 hours
