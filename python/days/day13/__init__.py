def parse_input(fp):
    dots = set()
    folds = []
    dot_mode = True
    for line in open(fp, 'r').readlines():
        if dot_mode:
            try:
                dots.add(tuple(map(int, line.strip().split(','))))
            except ValueError:
                dot_mode = False
        else:
            fold = line.strip().split(' ')[-1]
            fold_directions = fold.split('=')
            folds.append((fold_directions[0], int(fold_directions[1])))
    return dots, folds


def fold_paper(dots, fold):
    direction, line = fold
    dots_to_remove = set()
    dots_to_add = set()
    if direction == 'x':
        for x, y in dots:
            if x > line:
                dots_to_remove.add((x, y))
                dots_to_add.add((2 * line - x, y))
    else:  # y
        for x, y in dots:
            if y > line:
                dots_to_remove.add((x, y))
                dots_to_add.add((x, 2 * line - y))
                
    dots -= dots_to_remove
    dots |= dots_to_add


def print_dots(dots):
    max_x = max(dots, key=lambda x: x[0])[0]
    max_y = max(dots, key=lambda x: x[1])[1]
    print(max_x, max_y)
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if (x,y) in dots:
                print('|#|', end='')
            else:
                print('   ', end='')
        print('\n')

def solve():
    dots, folds = parse_input('../input/day13')  # dots are (x, y)
    for fold in folds[:1]:
        fold_paper(dots, fold)
        part_1_solution = len(dots)
    for fold in folds[1:]:
        fold_paper(dots, fold)

    print_dots(dots)
    return part_1_solution, 0