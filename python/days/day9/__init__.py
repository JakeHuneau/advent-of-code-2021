from itertools import product

def check_neighbor(height_maps, curr_height, y, x):
    if y == -1 or x == -1:
        return True
    try:
        return curr_height < height_maps[y][x]
    except IndexError:
        return True

def get_low_points(height_maps):
    low_points = []
    for i, j in product(range(len(height_maps)), range(len(height_maps[0]))):
        low_point = True
        for neighbor in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if not check_neighbor(height_maps, height_maps[i][j], neighbor[0], neighbor[1]):
                low_point = False
        if low_point:
            low_points.append((i, j))
    return low_points

def add_basin_points(height_maps, curr_point, basin_points):
    y, x = curr_point
    curr_value = height_maps[y][x]
    if curr_value == '9':
        return
    else:
        basin_points.add(curr_point)
    if y != 0 and height_maps[y-1][x] > curr_value:  # up
        add_basin_points(height_maps, (y-1, x), basin_points)
    if y != len(height_maps) - 1 and height_maps[y+1][x] > curr_value:  # down
        add_basin_points(height_maps, (y+1, x), basin_points)
    if x != 0 and height_maps[y][x-1] > curr_value:  # left
        add_basin_points(height_maps, (y, x-1), basin_points)
    if x != len(height_maps[0]) - 1 and height_maps[y][x+1] > curr_value:  # right
        add_basin_points(height_maps, (y, x+1), basin_points)

def part_2(height_maps, low_points):
    basins = []
    for low_point in low_points:
        basin_points = set()
        add_basin_points(height_maps, low_point, basin_points)
        basins.append(len(basin_points))
    sorted_basins = sorted(basins)
    return sorted_basins[-1] * sorted_basins[-2] * sorted_basins[-3]

def solve():
    height_maps = [l.strip() for l in open("../input/day9", "r")]
    low_points = get_low_points(height_maps)
    return sum(int(height_maps[i][j]) + 1 for i, j in low_points), part_2(height_maps, low_points)