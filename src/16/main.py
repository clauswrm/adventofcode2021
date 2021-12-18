from typing import List, Tuple
from numpy import product


def read_input(file_path: str) -> List[str]:
    with open(file_path) as f:
        file_content = f.read().splitlines()
        return file_content


def main(data: str, print_packet_verison_sum: bool = False):
    bin_data = "".join(['{0:04b}'.format(int(c, 16)) for c in data])
    _, value = read_packet(bin_data)
    if print_packet_verison_sum:
        print(packet_version_sum)
    else:
        print(value)


def read_packet(packet: str, i: int = 0) -> Tuple[int, int]:
    packet_version, packet_id = int(packet[i:i+3], 2), int(packet[i+3:i+6], 2)
    global packet_version_sum
    packet_version_sum += packet_version
    i += 6
    if packet_id == 4:
        literal = ""
        group = packet[i:i+5]
        prefix = group[0]
        literal += group[1:]
        i += 5
        while prefix == "1":
            group = packet[i:i+5]
            prefix = group[0]
            literal += group[1:]
            i += 5
        digit = int(literal, 2)
        return i, digit
    else:
        functions = [sum, product, min, max, None, lambda l: int(
            l[0] > l[1]), lambda l: int(l[0] < l[1]), lambda l: int(l[0] == l[1])]
        length_type_id = packet[i]
        i += 1
        values = []
        if length_type_id == "0":
            sub_packet_length = int(packet[i:i+15], 2)
            i += 15
            sub_packets_end = i + sub_packet_length
            while i < sub_packets_end:
                i, value = read_packet(packet, i)
                values.append(value)
        else:
            sub_packet_count = int(packet[i:i+11], 2)
            i += 11
            for _ in range(sub_packet_count):
                i, value = read_packet(packet, i)
                values.append(value)
        return i, functions[packet_id](values)


if __name__ == "__main__":
    # Task 1
    file_content = read_input("src/16/data.txt")
    packet_version_sum = 0
    main(file_content[0], print_packet_verison_sum=True)
    # Task 2
    main(file_content[0])
