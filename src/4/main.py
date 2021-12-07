from typing import List


def read_input(file_path: str) -> List[str]:
    with open(file_path) as f:
        file_content = f.read().splitlines()
        return file_content


def main(data: List[str], last=False):
    drawings, *boards = data
    drawings = [int(n) for n in drawings.split(",")]
    bingo_lists: List[List[List[int]]] = []
    for i in range(0, len(boards), 6):
        bingo_rows = [[int(n) for n in boards[j].split()]
                      for j in range(i + 1, i + 6)]
        bingo_cols = [[int(boards[l].split()[k])
                       for l in range(i + 1, i + 6)] for k in range(5)]
        bingo_lists.append(bingo_rows + bingo_cols)

    has_won = [0] * len(bingo_lists)

    for n in drawings:
        for player, bingo_board_list in enumerate(bingo_lists):
            for lst in bingo_board_list:
                for i in range(5):
                    if lst[i] == n:
                        lst[i] = -1

                if sum(lst) == -5:
                    winning_sum = sum([sum(filter(lambda p: p > 0, lst2))
                                      for lst2 in bingo_board_list]) // 2
                    if not last:
                        print(winning_sum * n)
                        return
                    else:
                        has_won[player] = 1
                        if sum(has_won) == len(bingo_lists):
                            print(winning_sum * n)
                            return


if __name__ == "__main__":
    # Task 1
    file_content = read_input("src/4/data.txt")
    main(file_content)
    # Task 2
    main(file_content, last=True)
