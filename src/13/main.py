from typing import List, Tuple
import numpy as np


def read_input(file_path: str) -> List[str]:
    with open(file_path) as f:
        file_content = f.read().splitlines()
        return file_content


def main(data: List[str], first_fold_only: bool = False):
    fold_instructions: List[Tuple[str, int]] = []
    first_x_fold, first_y_fold = 0, 0
    for line in data:  # Read fold instructions
        if "=" in line:
            *_, folding = line.split()
            fold_dir, fold_row = folding.split("=")
            fold_instructions.append((fold_dir, int(fold_row)))
            if first_x_fold == 0 and fold_dir == "x":
                first_x_fold = int(fold_row)
            if first_y_fold == 0 and fold_dir == "y":
                first_y_fold = int(fold_row)

    dots = np.zeros((first_y_fold*2+1, first_x_fold*2+1), dtype=bool)
    for line in data:  # Read dot placements
        if "," in line:
            x, y = line.split(",")
            x, y = int(x), int(y)
            dots[y, x] = True

    if first_fold_only:
        fold_instructions = fold_instructions[:1]
    for f_dir, f_row in fold_instructions:
        if f_dir == "x":
            dots_temp = dots[:, :f_row]
            dots_temp |= np.flip(dots[:, f_row+1:], axis=1)
        else:
            dots_temp = dots[:f_row, :]
            dots_temp |= np.flip(dots[f_row+1:, :], axis=0)
        dots = dots_temp

    if first_fold_only:
        print(dots.sum())
    else:
        print_matrix(dots)


def print_matrix(matrix: np.ndarray):
    for row in matrix:
        print("".join(["#" if n else " " for n in row]))


if __name__ == "__main__":
    # Task 1
    file_content = read_input("src/13/data.txt")
    main(file_content, first_fold_only=True)
    # Task 2
    main(file_content)
