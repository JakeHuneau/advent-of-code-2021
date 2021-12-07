def get_num_fish(days, init_fish=None):
    """
    Using an that tracks how many fish are at each age, decrease the
    age each day, and if the age is 0 after a day finishes, cycle it over
    """
    init_age = 8
    reset_age = 6
    fish_timers = [0] * (init_age + 1)
    if init_fish:
        fish_timers = init_fish
    else:
        for line in open("../input/day6", 'r'):
            timers = line.split(',')
            for timer in timers:
                fish_timers[int(timer)] += 1

    for _ in range(days):
        fish_deliveries = fish_timers[0]
        for age in range(1, init_age + 1):
            fish_timers[age - 1] = fish_timers[age]
        fish_timers[reset_age] += fish_deliveries
        fish_timers[init_age] = fish_deliveries

    return sum(fish_timers), fish_timers

def solve():
    part_1_sum, fish_timers = get_num_fish(80)
    part_2_sum, _ = get_num_fish(256 - 80, fish_timers)
    return part_1_sum, part_2_sum
