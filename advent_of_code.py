import time
import sys

from days.day1 import solve as day1
from days.day2 import solve as day2
from days.day3 import solve as day3
from days.day4 import solve as day4
from days.day5 import solve as day5
from days.day6 import solve as day6
from days.day7 import solve as day7
from days.day8 import solve as day8
from days.day9 import solve as day9
from days.day10 import solve as day10
from days.day11 import solve as day11
from days.day12 import solve as day12
from days.day13 import solve as day13
from days.day14 import solve as day14
from days.day15 import solve as day15
from days.day16 import solve as day16
from days.day17 import solve as day17
from days.day18 import solve as day18
from days.day19 import solve as day19
from days.day20 import solve as day20
from days.day21 import solve as day21
from days.day22 import solve as day22
from days.day23 import solve as day23
from days.day24 import solve as day24
from days.day25 import solve as day25

def runtime(func):
    t1 = time.time()
    part_1, part_2 = func()
    t2 = time.time()
    print(f'part 1: {part_1}\npart 2: {part_2}\nTotal time: {(t2 - t1) * 1000:.3f} ms')

def test(day):
    days = [day1, day2, day3, day4, day5, day6, day7, day8, day9, day10,
        day11, day12, day13, day14, day15, day16, day17, day18, day19, 
        day20, day21, day22, day23, day24, day25]
    try:
        runtime(days[day-1])
    except IndexError:
        print("This day is not available. Days 1-25 are available.")
        
if __name__ == '__main__':
    try:
        day = int(sys.argv[1])
        test(day)
    except IndexError:
        print("Format is `python advent_of_code.py <day>`")
    except ValueError:
        print("Format is `python advent_of_code.py <day>` where <day> is a number from 1-25")
