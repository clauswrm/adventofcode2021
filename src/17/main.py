from typing import List


def read_input(file_path: str) -> List[str]:
    with open(file_path) as f:
        file_content = f.read().splitlines()
        return file_content


def main(data: str):
    x_min, x_max, y_min, y_max = map(int, filter(lambda s: s.lstrip("-").isdigit(),
                                                 data.replace("..", "=").replace(",", "=").split("=")))
    y_highest, hit_count = 0, 0
    for v0x in range(1, x_max + 1):
        for v0y in range(-1000, 1000):
            y_highest_current_shot = 0
            for x, y in shoot(v0x, v0y, y_min, x_max):
                if y > y_highest_current_shot:
                    y_highest_current_shot = y
                if x_min <= x <= x_max and y_min <= y <= y_max:
                    hit_count += 1
                    if y_highest_current_shot > y_highest:
                        y_highest = y_highest_current_shot
                    break
    print(y_highest, hit_count, sep="\n")


def shoot(v0x: int, v0y: int, y_min: int, x_max: int):
    x, y, = 0, 0
    vx, vy = v0x, v0y
    while y >= y_min and x <= x_max:
        x, y = x + vx, y + vy
        vx -= 1 if vx > 0 else -1 if vx < 0 else 0
        vy -= 1
        yield x, y


if __name__ == "__main__":
    # Task 1 and 2
    file_content = read_input("src/17/data.txt")
    main(file_content[0])
