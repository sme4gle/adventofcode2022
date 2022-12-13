from typing import List


def open_file() -> List[int]:
    elfs = [int]
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            try:
                value = int(line)
                elf_calories += value
            except:
                elf_calories = 0
            if elf_calories:
                elfs.append(elf_calories)
    return elfs


if __name__ == '__main__':
    elfs = open_file()
    # Part A
    print(max(elfs))

    # Part B
    top_cals = 0
    for e in range(3):
        top_cals += max(elfs)
        elfs.remove(max(elfs))
        print(top_cals)
    print(top_cals)
