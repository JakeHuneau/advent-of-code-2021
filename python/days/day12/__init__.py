from collections import defaultdict
from functools import lru_cache

class Cave:
    def __init__(self, file: str):
        self.neighbors = defaultdict(list)
        for path in [l.strip().split('-') for l in open(file).readlines()]:
            self.neighbors[path[0]].append(path[1])
            self.neighbors[path[1]].append(path[0])

    @lru_cache
    def dfs(self, current_cave: str, visited_caves: set[str], visited_small=True) -> int:
        if current_cave.islower():
            visited_caves |= {current_cave}
        num_paths = 0
        for destination in self.neighbors[current_cave]:
            if destination == 'end':
                num_paths += 1
            elif destination != 'start':
                if destination not in visited_caves:
                    num_paths += self.dfs(destination, visited_caves, visited_small)
                elif not visited_small:
                    num_paths += self.dfs(destination, visited_caves, True)
        return num_paths


def solve():
    cave = Cave("../input/day12")
    return cave.dfs('start', frozenset()), cave.dfs('start', frozenset(), False)