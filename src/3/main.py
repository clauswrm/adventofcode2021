from typing import List


def read_input(file_path: str) -> List[str]:
    with open(file_path) as f:
        file_content = f.read().splitlines()
        return file_content


def main_1(data: List[str]):
    rate1 = ""
    rate2 = ""
    for i in range(len(data[0])):
        k = 0
        for j in range(len(data)):
            k += int(data[j][i])
        if k < len(data) / 2:
            rate1 += "0"
            rate2 += "1"
        else:
            rate1 += "1"
            rate2 += "0"
    print(int(rate1, 2) * int(rate2, 2))


def main_2(data: List[str], index: int, tiebreaker: int):
    if len(data) == 1:
        print(int(data[0], 2))
        return
    sum_of_nums = sum(map(lambda row: int(row[index]), data))
    if sum_of_nums > len(data) / 2:
        main_2(list(filter(lambda row: int(row[index]) == tiebreaker, data)), index + 1, tiebreaker)
    elif sum_of_nums < len(data) / 2:
        main_2(list(filter(lambda row: int(row[index]) == int(
            not tiebreaker), data)), index + 1, tiebreaker)
    else:
        main_2(list(filter(lambda row: int(row[index]) == tiebreaker, data)), index + 1, tiebreaker)


if __name__ == "__main__":
    # Task 1
    file_content = read_input("src/3/data.txt")
    main_1(file_content)
    # Task 2 - multiply output manually
    main_2(file_content, 0, 0)
    main_2(file_content, 0, 1)
