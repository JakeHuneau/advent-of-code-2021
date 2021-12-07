from functools import cache

def mean(data: list[int]) -> int:
    return sum(d/len(data) for d in data)

def median(data: list[int]) -> int:
    sorted_data = sorted(data)
    if len(data) % 2 == 1:
        # Odd length, return middle value
        return sorted_data[int(len(data) / 2)]
    # Otherwise, even so take average of middle 2 values
    middle_index = int(len(data) / 2)
    return round((sorted_data[middle_index] + sorted_data[middle_index - 1]) / 2)

@cache
def part_2_cost(distance: int) -> int:
    """
    sum(1, n) = n(n+1)/2
    """
    return int((distance * (distance + 1)) / 2)

def solve() -> tuple[int, int]:
    with open('../input/day7', 'r') as f:
        crabs = [int(x) for x in f.read().strip().split(',')]
    median_crab = round(median(crabs))

    # Solution is between floor(mean) - ceil(mean). Calculate both and find min at end
    mean_crab = mean(crabs)
    mean_crab_floor = int(mean_crab)
    mean_crab_ceil = round(mean_crab)

    total_fuel_part_1 = 0
    total_fuel_part_2_floor = 0
    total_fueld_part_2_ceil = 0

    for crab in crabs:
        total_fuel_part_1 += abs(crab - median_crab)
        total_fuel_part_2_floor += part_2_cost(abs(crab - mean_crab_floor))
        if (mean_crab_floor != mean_crab_ceil):
            total_fueld_part_2_ceil += part_2_cost(abs(crab - mean_crab_ceil))

    if (mean_crab_floor != mean_crab_ceil):
        part_2_fuel_cost = min(total_fuel_part_2_floor, total_fueld_part_2_ceil)
    else:
        part_2_fuel_cost = total_fuel_part_2_floor

    return total_fuel_part_1, part_2_fuel_cost
