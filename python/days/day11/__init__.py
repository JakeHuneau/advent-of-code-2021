from itertools import product
from pprint import pprint

EnergyLevels = list[list[int]]

def single_step(energy_levels: EnergyLevels) -> int:
    """
    returns number of flashes then new energy_levels
    """
    flashes = 0
    need_to_check = True
    for i, j in product(range(len(energy_levels)), range(len(energy_levels[0]))):
        # First increase everything by 1
        if energy_levels[i][j] < 0:
            energy_levels[i][j] = 1
        else:
            energy_levels[i][j] += 1
    while need_to_check:
        need_to_check = False
        for i, j in product(range(len(energy_levels)), range(len(energy_levels[0]))):
            if energy_levels[i][j] > 9:
                need_to_check = True
                flashes += 1
                energy_levels[i][j] = -1000 # Reset to super low value
                for neighbor in [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]:
                    if neighbor[0] < 0 or neighbor[1] < 0:
                        continue
                    try:
                        energy_levels[neighbor[0]][neighbor[1]] += 1
                    except IndexError:
                        continue
    return flashes

def first_full_flash(energy_levels: EnergyLevels) -> int:
    steps = 0
    while True:
        full_flash = True
        for i, j in product(range(len(energy_levels)), range(len(energy_levels[0]))):
            if energy_levels[i][j] > 0:
                full_flash = False
                break
        if full_flash:
            return steps
        single_step(energy_levels)
        steps += 1

def solve() -> tuple[int, int]:
    energy_levels = [[int(i) for i in l.strip()] for l in open('../input/day11', 'r').readlines()]
    flashes = 0
    for _ in range(100):
        flashes += single_step(energy_levels)
    return flashes, first_full_flash(energy_levels) + 100