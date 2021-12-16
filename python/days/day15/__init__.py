from math import inf


def dijkstra(danger_levels):  # improve with a*
    q = [(0,0,0)]
    costs = {}
    while True:
        cost, x, y = q[0]
        if x==len(danger_levels)-1 and y==len(danger_levels[0])-1:
            return cost
        q = q[1:]
        for xx, yy in [(x+1,y),(x-1,y),(x,y-1),(x,y+1)]:
            try:
                new_cost = cost + danger_levels[xx][yy]
            except IndexError:
                continue
            if costs.get((xx,yy), inf) <= new_cost:
                continue
            costs[(xx, yy)] = new_cost
            q.append((new_cost, xx, yy))
        q = sorted(q)


def make_big_list(danger_levels, steps):
    big_list = [[0 for i in range(steps * len(danger_levels[0]))] for j in range(steps * len(danger_levels))]
    for i in range(len(big_list)):
        for j in range(len(big_list[0])):
            tile_number = i // len(danger_levels) + j // len(danger_levels[0])
            val = danger_levels[i % len(danger_levels)][j % len(danger_levels)]
            for _ in range(tile_number):
                val += 1
                if val == 10:
                    val = 1
            big_list[i][j] = val
    return big_list


def solve():
    danger_levels = [list(map(int, x.strip())) for x in open('../input/day15', 'r').readlines()]
    big_danger_levels = make_big_list(danger_levels, 5)
    return dijkstra(danger_levels), dijkstra(big_danger_levels)
