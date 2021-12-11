from typing import List, Union
import numpy as np
from collections import defaultdict


def read_input(file_path: str) -> List[str]:
    with open(file_path) as f:
        file_content = f.read().splitlines()
        return file_content


def main_1(data: List[str]):
    matrix = np.array(list(map(lambda l: [int(c) for c in l], data)))
    total = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            is_low_point = True
            if i > 0:
                if matrix[i][j] >= matrix[i-1][j]:
                    is_low_point = False
            if i < matrix.shape[0] - 1:
                if matrix[i][j] >= matrix[i+1][j]:
                    is_low_point = False
            if j > 0:
                if matrix[i][j] >= matrix[i][j-1]:
                    is_low_point = False
            if j < matrix.shape[1] - 1:
                if matrix[i][j] >= matrix[i][j+1]:
                    is_low_point = False
            if is_low_point:
                total += matrix[i][j] + 1
    print(total)


class Node:
    """ Class that represents a node in a tree """

    i = 0  # Class vaiable used to uniquely name each node

    def __init__(self, x, y):
        """ Constructs a node from the cell at coordinates (x, y) """
        self.coord = (x, y)
        self.parent = self
        self.rank = 0
        self.name = Node.i  # Names start at ASCII 65 = 'A'
        Node.i += 1

    def find_set(self):
        """ Finds the parent of the node, thereby flattening the tree structure """
        if self.parent != self:
            self.parent = self.parent.find_set()
        return self.parent

    @staticmethod
    def link(own_parent, other_parent):
        """ Joins two trees by making one parent the parent of the other based on their rank """
        if own_parent.rank > other_parent.rank:
            other_parent.parent = own_parent
        else:
            own_parent.parent = other_parent
            if own_parent.rank == other_parent.rank:
                other_parent.rank += 1

    def union(self, other):
        """ Finds the parent of both nodes and joins their trees """
        if self.parent != other.parent:
            self.link(self.find_set(), other.find_set())

    def __bool__(self):
        """ Used in make_set_forest to make sure there is a node """
        return True

    def parent_name(self):
        """ Returns the name of the parent node """
        return self.find_set().name


def groupify(binary_matrix: np.ndarray):
    set_matrix: List[List[Union[Node, None]]] = [[None for _ in range(
        binary_matrix.shape[1])] for _ in range(binary_matrix.shape[0])]

    for i, row in enumerate(binary_matrix):
        for j, cell in enumerate(row):
            if cell == 1:
                set_matrix[i][j] = Node(j, i)

    for i, row in enumerate(set_matrix):
        for j, node in enumerate(row):
            if node:
                if i > 0:
                    if set_matrix[i-1][j]:
                        node.union(set_matrix[i-1][j])
                if i < binary_matrix.shape[0] - 1:
                    if set_matrix[i+1][j]:
                        node.union(set_matrix[i+1][j])
                if j > 0:
                    if set_matrix[i][j-1]:
                        node.union(set_matrix[i][j-1])
                if j < binary_matrix.shape[1] - 1:
                    if set_matrix[i][j+1]:
                        node.union(set_matrix[i][j+1])
    return set_matrix


def main_2(data: List[str]):
    matrix = np.array(list(map(lambda l: [int(c) for c in l], data)))
    set_matrix = groupify((matrix < 9).astype(int))

    basin_sizes = defaultdict(int)
    for row in set_matrix:
        for cell in row:
            if cell:
                basin_sizes[cell.parent_name()] += 1
    basin_sizes_sorted = sorted(basin_sizes.values(), reverse=True)
    print(basin_sizes_sorted[0]*basin_sizes_sorted[1]*basin_sizes_sorted[2])


if __name__ == "__main__":
    # Task 1
    file_content = read_input("src/9/data.txt")
    main_1(file_content)
    # Task 2
    main_2(file_content)
