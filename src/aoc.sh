#!/bin/bash
set -e

mkdir -p "src/$1"

if [ ! -f "src/$1/data.txt" ]; then
    touch "src/$1/data.txt"
    curl -s --cookie "session=$(grep 'SESSION_COOKIE' .env | awk -F '=' '{print $2}')" https://adventofcode.com/2021/day/$1/input > "src/$1/data.txt"
fi

if [ ! -f "src/$1/main.py" ]; then
    touch "src/$1/main.py"
    cat <<EOF > src/$1/main.py
from typing import List
import numpy as np


def read_input(file_path: str) -> List[str]:
    with open(file_path) as f:
        file_content = f.read().splitlines()
        return file_content

def main(data: List[str]):
    pass

if __name__ == "__main__":
    # Task 1
    file_content = read_input("src/$1/data.txt")
    main(file_content)
    # Task 2
    pass
EOF
fi
