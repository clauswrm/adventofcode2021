from typing import List


def read_input(file_path: str) -> List[str]:
    with open(file_path) as f:
        file_content = f.read().splitlines()
        return file_content


def main_1(data: List[str]):
    x_pos, y_pos = 0, 0
    for command in data:
        direction, unit = command.split()
        if direction == "forward":
            x_pos += int(unit)
        elif direction == "down":
            y_pos += int(unit)
        elif direction == "up":
            y_pos -= int(unit)
    print(x_pos * y_pos)


def main_2(data: List[str]):
    x_pos, y_pos, aim = 0, 0, 0
    for command in data:
        direction, unit = command.split()
        if direction == "forward":
            x_pos += int(unit)
            y_pos += aim * int(unit)
        elif direction == "down":
            aim += int(unit)
        elif direction == "up":
            aim -= int(unit)
    print(x_pos * y_pos)


if __name__ == "__main__":
    # Task 1
    file_content = read_input("src/2/data.txt")
    main_1(file_content)
    # Task 2
    main_2(file_content)
