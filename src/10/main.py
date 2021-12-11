from typing import List
from functools import reduce


def read_input(file_path: str) -> List[str]:
    with open(file_path) as f:
        file_content = f.read().splitlines()
        return file_content


pair = {"(": ")", "[": "]", "{": "}", "<": ">"}


def main_1(data: List[str]):
    total = 0
    points = {")": 3, "]": 57, "}": 1197, ">": 25137}

    for line in data:
        stack: List[str] = []
        for char in line:
            if char in "([{<":
                stack.append(char)
            else:
                for bracket in "([{<":
                    if char == pair[bracket]:
                        if stack[-1] == bracket:
                            stack.pop()
                        else:
                            total += points[char]
                            break
                else:
                    continue
                break  # If we broke out of inner loop, break outer loop aswell
    print(total)


def main_2(data: List[str]):
    scores: List[int] = []
    points = {")": 1, "]": 2, "}": 3, ">": 4}

    for line in data:
        stack: List[str] = []
        is_corrupted = False
        for char in line:
            if char in "([{<":
                stack.append(char)
            else:
                for bracket in "([{<":
                    if char == pair[bracket]:
                        if stack[-1] == bracket:
                            stack.pop()
                        else:
                            is_corrupted = True

        if not is_corrupted:
            scores.append(reduce(lambda a, b: a * 5 + b,
                                 map(lambda b: points[pair[b]], reversed(stack)), 0))

    scores.sort()
    print(scores[len(scores) // 2])


if __name__ == "__main__":
    # Task 1
    file_content = read_input("src/10/data.txt")
    main_1(file_content)
    # Task 2
    main_2(file_content)
