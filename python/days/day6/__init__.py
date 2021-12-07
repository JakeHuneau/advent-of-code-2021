def get_num_fish(days):
    """
    Using an that tracks how many fish are at each age, decrease the
    age each day, and if the age is 0 after a day finishes, cycle it over
    """
    init_age = 8
    reset_age = 6
    fish_timers = [0] * (init_age + 1)
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

    return sum(fish_timers)

def solve():
    return get_num_fish(80), get_num_fish(256)
