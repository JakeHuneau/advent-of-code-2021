# --- Day 3: Binary Diagnostic ---
from types import EllipsisType


def get_input():
    return [line.strip() for line in open("../input/day3", "r")]

def binary_flip(data):
    """
    Flips 1 -> 0, 0 -> 1 for all bits
    """
    return ['0' if d == '1' else '1' for d in data]

def get_gamma(data, equality):
    """
    Gets the gamma value by counting the 1's in each place and then 
    comparing that to the total number of numbers to determine if 1 is
    more common
    """
    binary_count = None
    total_numbers = 0
    for num in data:
        total_numbers += 1
        if not binary_count:
            binary_count = [int(bit) for bit in num]  # initialize with all values
            continue
        for index, bit in enumerate(num):
            binary_count[index] += int(bit)

    if equality:
        return ['1' if bit_count >= total_numbers / 2 else '0' for bit_count in binary_count]
    return ['1' if bit_count > total_numbers / 2 else '0' for bit_count in binary_count]

def get_gamma_epsilon(data, equality=False):
    """
    epsilon is just a binary flip of gamma
    """
    gamma = get_gamma(data, equality)
    epsilon = binary_flip(gamma)
    return ''.join(gamma), ''.join(epsilon)

def part_1(data):
    gamma, epsilon = get_gamma_epsilon(data)
    return int(gamma, 2) * int(epsilon, 2)

def part_2(data):
    """
    Need to recalculate gamma and epsilon after each filtering
    """
    o2_list = [d for d in data]
    o2_index = 0

    co2_list = [d for d in data]
    co2_index = 0

    while len(o2_list) > 1:
        gamma, _ = get_gamma_epsilon(o2_list, True)
        o2_list = list(filter(lambda o2: o2[o2_index] == gamma[o2_index], o2_list))
        o2_index += 1

    while len(co2_list) > 1:
        _, epsilon = get_gamma_epsilon(co2_list, True)
        co2_list = list(filter(lambda co2: co2[co2_index] == epsilon[co2_index], co2_list))
        co2_index += 1

    return int(o2_list[0], 2) * int(co2_list[0], 2)

def solve():
    data = get_input()
    return part_1(data), part_2(data)
