from typing import Callable, List


def read_input(file_path: str) -> List[str]:
    with open(file_path) as f:
        file_content = f.read().splitlines()
        return file_content


def main(data: List[str], cost_function: Callable[[int], int]):
    crabs = list(map(int, data[0].split(",")))
    best_yet = 10e10
    for i in range(1000):
        x = sum(map(cost_function, map(lambda c: c-i, crabs)))
        if x < best_yet:
            best_yet = x
    print(best_yet)


if __name__ == "__main__":
    # Task 1
    file_content = read_input("src/7/data.txt")
    main(file_content, lambda c: abs(c))
    # Task 2
    main(file_content, lambda c: abs(c) * (abs(c)+1) // 2)
