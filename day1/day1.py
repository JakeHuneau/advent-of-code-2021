def part_1():
    prev_num = None
    tot_increases = 0

    # part 1
    for num in open('day1/data', 'r'):
        if prev_num:
            if int(num) > prev_num:
                tot_increases += 1
        prev_num = int(num)
    
    print(f'part 1: {tot_increases}')

def part_2():
    window_size = 3
    window = [None] * window_size
    slider = 0

    tot_increases = 0

    for num in open('day1/data', 'r'):
        if window[window_size - 1]:
            if int(num) > window[slider]:
                tot_increases += 1
        window[slider] = int(num)
        slider = (slider + 1) % window_size

    print(f'part 2: {tot_increases}')

if __name__ == '__main__':
    part_1()
    part_2()
