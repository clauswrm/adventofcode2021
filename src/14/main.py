from itertools import product
from typing import List
import numpy as np


def read_input(file_path: str) -> List[str]:
    with open(file_path) as f:
        file_content = f.read().splitlines()
        return file_content


def main(data: List[str], iterations: int):
    polymer, _, *rules = data
    insertion_rules = [(rule.split(" ")[0], rule.split(" ")[2]) for rule in rules]
    unique_chars = "".join(set(filter(lambda char: char.isalpha(), map(lambda pair: pair[1], insertion_rules))))
    char_to_index = {char: index for index, char in enumerate(unique_chars)}
    memo = {"".join(pair): np.zeros((iterations + 1, len(unique_chars)), dtype=np.int64)
            for pair in product(unique_chars, repeat=2)}
    for i in range(1, iterations + 1):
        for pattern, insert in insertion_rules:
            left, right = pattern[0] + insert, insert + pattern[1]
            initial = [0] * len(unique_chars)
            initial[char_to_index[insert]] += 1
            memo[pattern][i] = np.array(initial, dtype=np.int64) + memo[left][i-1] + memo[right][i-1]
    element_counts: np.ndarray = sum([memo["".join(char_pair)][iterations]
                                     for char_pair in zip(polymer, polymer[1:])])  # type: ignore
    for p in polymer:
        element_counts[char_to_index[p]] += 1
    print(element_counts.max() - element_counts.min())


if __name__ == "__main__":
    # Task 1
    file_content = read_input("src/14/data.txt")
    main(file_content, iterations=10)
    # Task 2
    main(file_content, iterations=40)
