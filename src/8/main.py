from typing import List


def read_input(file_path: str) -> List[str]:
    with open(file_path) as f:
        file_content = f.read().splitlines()
        return file_content


def main_1(data: List[str]):
    counter = [0] * 10
    for line in data:
        _, output_values = line.split("|")
        output_values = output_values.split()
        for val in output_values:
            counter[len(val)] += 1
    print(counter[2]+counter[3]+counter[4]+counter[7])


def main_2(data: List[str]):
    total = 0
    for line in data:
        signals, output_values = line.split("|")
        signals = signals.split()
        output_values = output_values.split()
        posibilities = dict()
        one = list(filter(lambda s: len(s) == 2, signals))[0]
        posibilities["a"] = [c for c in one]
        posibilities["b"] = [c for c in one]
        seven = list(filter(lambda s: len(s) == 3, signals))[0]
        posibilities["d"] = [c for c in seven if c not in one]
        four = list(filter(lambda s: len(s) == 4, signals))[0]
        posibilities["e"] = [c for c in four if c not in one]
        zerosixnine = list(filter(lambda s: len(s) == 6, signals))
        zero = list(filter(lambda s: (posibilities["e"][0] not in s) or (
            posibilities["e"][1] not in s), zerosixnine))[0]
        sixnine = list(filter(lambda s: (posibilities["e"][0] in s) and (
            posibilities["e"][1] in s), zerosixnine))
        posibilities["f"] = [c for c in ["a", "b", "c", "d", "e", "f", "g"] if c not in zero]
        posibilities["e"].remove(posibilities["f"][0])
        six = list(filter(lambda s: (posibilities["a"][0] not in s) or (
            posibilities["a"][1] not in s), sixnine))[0]
        posibilities["a"] = [c for c in ["a", "b", "c", "d", "e", "f", "g"] if c not in six]
        posibilities["b"].remove(posibilities["a"][0])
        sixnine.remove(six)
        nine = sixnine[0]
        posibilities["g"] = [c for c in ["a", "b", "c", "d", "e", "f", "g"] if c not in nine]
        taken = "".join(posibilities["a"] + posibilities["b"] + posibilities["d"] +
                        posibilities["e"] + posibilities["f"] + posibilities["g"])
        posibilities["c"] = [c for c in ["a", "b", "c", "d", "e", "f", "g"] if c not in taken]

        num_val = ""
        for val in output_values:
            if len(val) == 2:
                num_val += "1"
            if len(val) == 3:
                num_val += "7"
            if len(val) == 4:
                num_val += "4"
            if len(val) == 7:
                num_val += "8"
            if len(val) == 5:
                if posibilities["g"][0] in val:
                    num_val += "2"
                elif posibilities["e"][0] in val:
                    num_val += "5"
                else:
                    num_val += "3"
            if len(val) == 6:
                if posibilities["f"][0] not in val:
                    num_val += "0"
                elif posibilities["a"][0] in val:
                    num_val += "9"
                else:
                    num_val += "6"

        total += int(num_val)
    print(total)


if __name__ == "__main__":
    # Task 1
    file_content = read_input("src/8/data.txt")
    main_1(file_content)
    # Task 2
    main_2(file_content)
