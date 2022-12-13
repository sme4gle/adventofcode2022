from typing import List


def read_input() -> List:
    with open('input.txt', 'r') as f:
        return f.read().splitlines()

