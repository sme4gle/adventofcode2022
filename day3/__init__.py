from common import read_input

all_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
def day2() -> int:
    return 0

def calculate_character_value(letter: str) -> int:
    for val, c in enumerate(all_characters):
        if c == letter:
            return val + 1


def items_in_both_compartiments(comp_a: str, comp_b: str) -> str:
    _str = ''
    for x in all_characters:
        if x in comp_a and x in comp_b:
            _str += x
    return _str

if __name__ == '__main__':
    input = read_input()
    total_priority_sum = 0
    for rucksack in input:
        compartiment_a = rucksack[:int(len(rucksack) / 2)]
        compartiment_b = rucksack[int(len(rucksack) / 2):]

        items = items_in_both_compartiments(compartiment_a, compartiment_b)
        total_priority_sum += calculate_character_value(items)
    print(total_priority_sum)
