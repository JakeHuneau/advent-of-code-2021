# --- Day 2: Dive! ---

class Location:
    def __init__(self):
        self.horizontal = 0
        self.depth = 0
        self.aim = 0

    def handle_movement(self, movement, aim=False):
        """
        Handles a direction like 'forward x', 'down x', or 'up x'
        """
        match movement.split():
            case ["forward", distance]:
                self.horizontal += int(distance)
                if aim:
                    self.depth += self.aim * int(distance)
            case ["down", distance]:
                self.aim += int(distance)
                if not aim:
                    self.depth += int(distance)
            case ["up", distance]:
                self.aim -= int(distance)
                if not aim:
                    self.depth -= int(distance)

    def product(self):
        return self.horizontal * self.depth

def dive(aim=False):
    location = Location()
    for movement in open('days/day2/data', 'r'):
        location.handle_movement(movement, aim)
    return location.product()

def solve():
    return dive(), dive(True)