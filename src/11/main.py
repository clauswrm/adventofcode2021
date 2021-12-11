from typing import List
import numpy as np


def read_input(file_path: str) -> List[str]:
    with open(file_path) as f:
        file_content = f.read().splitlines()
        return file_content


def main(data: List[str], iterations=100, find_all_blink=False):
    total_flashes = 0
    octos = np.array([[int(o) for o in row] for row in data], dtype=int)
    for i in range(iterations):
        octos += 1
        flashes = np.zeros((octos.shape[0] + 2, octos.shape[1] + 2), dtype=int)
        old_flashes = flashes.copy()
        flashes[1:-1, 1:-1] = (octos > 9).astype(int)
        while not (old_flashes.sum() == flashes.sum()):
            old_flashes = flashes.copy()
            for y in range(octos.shape[0]):
                for x in range(octos.shape[1]):
                    if not flashes[y+1, x+1] == 1:
                        if octos[y, x] + flashes[y:y+3, x:x+3].sum() > 9:
                            flashes[y+1, x+1] = 1

        total_flashes += flashes.sum()
        for y in range(octos.shape[0]):
            for x in range(octos.shape[1]):
                octos[y, x] += flashes[y:y+3, x:x+3].sum()

        if find_all_blink and (octos > 9).all():
            print(i + 1)
            return

        octos[octos > 9] = 0
    print(total_flashes)


if __name__ == "__main__":
    # Task 1
    file_content = read_input("src/11/data.txt")
    main(file_content)
    # Task 2
    main(file_content, 500, find_all_blink=True)
