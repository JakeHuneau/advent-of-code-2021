from collections import defaultdict

def parse(fp):
    all_lines = open(fp).readlines()
    initial, rules = all_lines[0].strip(), [i.strip().split(' -> ') for i in all_lines[2:]]

    pairs = defaultdict(lambda: 0)
    for i in range(len(initial)-1):
        pairs[initial[i:i+2]] += 1

    rules = {i[0]: [i[0][0] + i[1], i[1] + i[0][1]] for i in rules}
    return pairs, rules

def step(pairs: dict, rules: dict):
    new_pairs = defaultdict(lambda: 0)
    for pair in pairs.items():
        if pair[0] in rules:
            rule_res = rules[pair[0]]
            new_pairs[rule_res[0]] += pairs[pair[0]]
            new_pairs[rule_res[1]] += pairs[pair[0]]
    return new_pairs

def solve():
    pairs, rules = parse('../input/day14')
    last_letter = list(pairs.keys())[-1][1]
    letter_counts = defaultdict(lambda: 0)
    letter_counts[last_letter] += 1

    for _ in range(10):
        pairs = step(pairs, rules)
    pair_items = list(pairs.items())
    for pair in pair_items:
        letter_counts[pair[0][0]] += pair[1]

    part_1_tot = max(letter_counts.values()) - min(letter_counts.values())

    for _ in range(30):
        pairs = step(pairs, rules)

    letter_counts = defaultdict(lambda: 0)
    letter_counts[last_letter] += 1
    pair_items = list(pairs.items())
    for pair in pair_items:
        letter_counts[pair[0][0]] += pair[1]

    return part_1_tot, max(letter_counts.values()) - min(letter_counts.values())