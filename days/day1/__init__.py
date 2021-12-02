def windowed_comparison(window_size: int):
    """
    When comparing the sum of a window vs the next window, we only need to look at the
    first value of the window vs the new value we're encountering.
    """
    window = [None] * window_size  # Start with None so we can start by building window
    slider = 0  # Where in the window we're at

    tot_increases = 0

    for num in open('days/day1/data', 'r'):
        if window[window_size - 1]:  # Skip first <window_size> values to build initial window
            if int(num) > window[slider]: 
                tot_increases += 1
        window[slider] = int(num)
        slider = (slider + 1) % window_size  # Move slider up and wrap around

    return tot_increases

def solve():
    return windowed_comparison(1), windowed_comparison(3)
