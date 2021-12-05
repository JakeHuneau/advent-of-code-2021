from collections import defaultdict

class Line:
    def __init__(self, start, end):
        self.start = start # (x,y)
        self.end = end # (x,y)
        self.straight = start[0] == end[0] or start[1] == end[1]
    
    def __repr__(self):
        return f'{self.start} -> {self.end} (straight: {self.straight})'

    def get_all_points(self):
        if self.start[0] < self.end[0]:
            x_change = lambda x, i: x + i
        elif self.start[0] == self.end[0]:
            x_change = lambda x, i: x
        else:
            x_change = lambda x, i: x - i

        if self.start[1] < self.end[1]:
                y_change = lambda y, i: y + i
        elif self.start[1] == self.end[1]:
            y_change = lambda y, i: y
        else:
            y_change = lambda y, i: y - i

        diff = max(abs(self.start[0] - self.end[0]), abs(self.start[1] - self.end[1]))
        return [(x_change(self.start[0], i), y_change(self.start[1], i)) for i in range(diff + 1)]


def parse_line(line):
    spl = line.split(' -> ')
    start, end = spl[0], spl[1]
    parse = lambda l: [int(x) for x in l.split(',')]
    return Line(parse(start), parse(end))


def solve():
    lines = list(map(parse_line, open('../input/day5', 'r')))
    straight_points_count = defaultdict(lambda: 0)
    all_points_count = defaultdict(lambda: 0)
    for line in lines:
        for point in line.get_all_points():
            all_points_count[point] += 1
            if line.straight:
                straight_points_count[point] += 1
    straight_crossings = len(list(filter(lambda x: x > 1, straight_points_count.values())))
    all_crossings = len(list(filter(lambda x: x > 1, all_points_count.values())))
    return straight_crossings, all_crossings