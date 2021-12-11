def get_points(line: str) -> tuple[int, int]:
    stack = []
    brackets = {')': '(', '}': '{', ']': '[', '>': '<'}
    points_invalid = {')': 3, ']': 57, '}': 1197, '>': 25137}
    points_remaining = {'(': 1, '[': 2, '{': 3, '<': 4}
    for bracket in line:
        if bracket not in brackets:
            stack.append(bracket)
        else:  # close bracket
            if stack[-1] != brackets[bracket]:
                return points_invalid[bracket], 0
            else:
                stack.pop(-1)
    remaining_tot = 0
    for bracket in stack[::-1]:
        remaining_tot *= 5
        remaining_tot += points_remaining[bracket]
    return 0, remaining_tot

def solve() -> tuple[int, int]:
    lines = [l.strip() for l in open('../input/day10', 'r').readlines()]
    part_1_tot = 0
    remaining_totals = []
    for res in map(get_points, lines):
        part_1_tot += res[0]
        if res[1] != 0:
            remaining_totals.append(res[1])

    return part_1_tot, sorted(remaining_totals)[int(len(remaining_totals) / 2)]