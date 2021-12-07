from typing import List


def read_input(file_path: str) -> List[str]:
    with open(file_path) as f:
        file_content = f.read().splitlines()
        return file_content


def simulate(fishes: List[int], days):
    for i in range(days//2):
        new_fishes: List[int] = []
        for fish in fishes:
            if fish == 0:
                new_fishes.append(6)
                new_fishes.append(8)
            else:
                new_fishes.append(fish - 1)
        fishes = new_fishes
    return fishes


def main(data: List[str], days: int = 80):
    fishes_after_half = []
    for i in range(9):
        fishes_after_half.append(len(simulate([i], days)))
    fishes = list(map(int, data[0].split(",")))
    out_fishes = simulate(fishes, days)
    total = 0
    for out_fish in out_fishes:
        total += fishes_after_half[out_fish]
    print(total)


if __name__ == "__main__":
    # Task 1
    file_content = read_input("src/6/data.txt")
    main(file_content, days=80)
    # Task 2
    main(file_content, days=256)
