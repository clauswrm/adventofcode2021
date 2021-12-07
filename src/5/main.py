from typing import List
import numpy as np


def read_input(file_path: str) -> List[str]:
    with open(file_path) as f:
        file_content = f.read().splitlines()
        return file_content


def main(data: List[str], consider_diags=True):
    matrix = np.zeros((1000, 1000), dtype=np.int32)
    for line in data:
        from_coords, _, to_coords = line.split(" ")
        f_x, f_y = map(int, from_coords.split(","))
        t_x, t_y = map(int, to_coords.split(","))
        if f_x == t_x:
            smallest_y, biggest_y = (f_y, t_y) if f_y < t_y else (t_y, f_y)
            for i in range(smallest_y, biggest_y + 1):
                matrix[f_x][i] += 1

        elif f_y == t_y:
            smallest_x, biggest_x = (f_x, t_x) if f_x < t_x else (t_x, f_x)
            for i in range(smallest_x, biggest_x + 1):
                matrix[i][f_y] += 1

        elif consider_diags:
            x_dir = 1 if f_x < t_x else -1
            y_dir = 1 if f_y < t_y else -1
            for i_x, i_y in zip(range(f_x, t_x + 1*x_dir, x_dir), range(f_y, t_y + 1*y_dir, y_dir)):
                matrix[i_x][i_y] += 1

    print((matrix > 1).sum())


if __name__ == "__main__":
    # Task 1
    file_content = read_input("src/5/data.txt")
    main(file_content, consider_diags=False)
    # Task 2
    main(file_content)
