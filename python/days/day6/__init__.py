from collections import defaultdict

def get_data():
    """
    Breaks the input into a dict that counts the number of fish at each age
    """
    fish_timers = defaultdict(lambda: 0)
    for line in open("../input/day6", 'r'):
        timers = line.split(',')
        for timer in timers:
            fish_timers[int(timer)] += 1
    return fish_timers

def get_num_fish(days):
    """
    Using a dict that tracks how many fish are at each age, decrease the
    age each day, and if the age is -1 at the end of the day, that fish
    has a baby and goes back to age 6
    """
    timers = get_data()
    init_age = 8
    reset_age = 6
    delivery_age = -1
    for _ in range(days):
        for age in range(init_age + 1):
            timers[age - 1] += timers[age]
            timers[age] = 0
        timers[reset_age] += timers[delivery_age]
        timers[init_age] += timers[delivery_age]
        timers[delivery_age] = 0
    return sum(timers.values())

def solve():
    return get_num_fish(80), get_num_fish(256)