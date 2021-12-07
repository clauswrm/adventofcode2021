from typing import List


def read_input(file_path: str) -> List[str]:
    with open(file_path) as f:
        file_content = f.read().splitlines()
        return file_content


def main(readings: List[int]):
    counter = 0
    for i in range(len(readings) - 1):
        if readings[i] < readings[i + 1]:
            counter += 1
    print(counter)


if __name__ == "__main__":
    # Task 1
    file_content = read_input("src/1/data.txt")
    readings = list(map(int, file_content))
    main(readings)
    # Task 2
    main([readings[i] + readings[i + 1] + readings[i + 2]
          for i in range(len(readings) - 2)])
