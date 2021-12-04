from multiprocessing import Pool

def parse_input():
    """
    Returns (list of numbers, list of boards which are 1D list where
    index 0:4 are first row, 5:9 are second, and so on for 5 rows)
    """
    bingo_numbers = []
    bingo_cards = []
    f = open("../input/day4")
    bingo_numbers = f.readline().strip().split(',')
    _ = f.readline()
    current_bingo_card = []
    for line in f.readlines():
        if line == '\n':
            # flush
            bingo_cards.append(current_bingo_card)
            current_bingo_card = []
        else:
            current_bingo_card.extend(line.strip().replace('  ', ' ').split(' '))
    bingo_cards.append(current_bingo_card)  # flush last card
    return bingo_numbers, bingo_cards

def mark_card(card, called_number):
    """
    Checks each number in the card and replaces it with 'x' if it matches
    """
    for index, card_number in enumerate(card):
        if card_number == called_number:
            card[index] = 'x'

def is_winner(card):
    """
    Winner if an entire row or column is x. Row would be indexes
    0:5, 5:10, 10:15, 15:20, or 20:25. Column would be indexes
    0,5,10,15,20; 1,6,11,16,21; 2,7,12,17,22; 3,8,13,18,23; or 4,9,14,19,24
    """
    winner_list = ['x'] * 5
    for i in range(5):
        if card[i*5:(i*5)+5] == winner_list:
            # Row
            return True
        if card[i::5] == winner_list:
            # Column
            return True
    return False

def sum_remaining_numbers(card):
    return sum(int(n) if n != 'x' else 0 for n in card)

def part_1():
    bingo_numbers, bingo_cards = parse_input()
    for number in bingo_numbers:
        for card in bingo_cards:
            mark_card(card, number)
            if is_winner(card):
                # Once we find a winner, return the solution
                return sum_remaining_numbers(card) * int(number)

def part_2():
    bingo_numbers, bingo_cards = parse_input()
    for number in bingo_numbers:
        num_cards = len(bingo_cards)
        for i in range(num_cards):
            # Go in reverse so we can pop from the end
            current_index = num_cards - (i + 1)
            current_card = bingo_cards[current_index]
            mark_card(current_card, number)
            if is_winner(current_card):
                # Once we find a winner, return the solution
                temp_card = bingo_cards.pop(current_index)
                if len(bingo_cards) == 0:
                    return sum_remaining_numbers(temp_card) * int(number)

def solve():
    return part_1(), part_2()