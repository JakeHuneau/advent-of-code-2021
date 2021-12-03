# --- Day 3: Binary Diagnostic ---
from types import EllipsisType


def get_input():
    return [line.strip() for line in open("../input/day3", "r")]

def binary_swap(data):
    return ['0' if d == '1' else '1' for d in data]

def get_gamma(data, equality):
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
    gamma = get_gamma(data, equality)
    epsilon = binary_swap(gamma)
    return ''.join(gamma), ''.join(epsilon)

def part_1(data):
    gamma, epsilon = get_gamma_epsilon(data)
    return int(gamma, 2) * int(epsilon, 2)

def part_2(data):
    o2_list = [d for d in data]
    o2_index = 0

    co2_list = [d for d in data]
    co2_index = 0

    while len(o2_list) > 1:
        gamma, epsilon = get_gamma_epsilon(o2_list, True)
        temp_o2_list = []
        for o2 in o2_list:
            if o2[o2_index] == gamma[o2_index]:
                temp_o2_list.append(o2)
        o2_list = temp_o2_list
        o2_index += 1
    o2_value = o2_list[0]

    while len(co2_list) > 1:
        gamma, epsilon = get_gamma_epsilon(co2_list, True)

        temp_co2_list = []
        for co2 in co2_list:
            if co2[co2_index] == epsilon[co2_index]:
                temp_co2_list.append(co2)
        co2_list = temp_co2_list
        co2_index += 1
    co2_value = co2_list[0]

    return int(o2_value, 2) * int(co2_value, 2)

def solve():
    data = get_input()
    return part_1(data), part_2(data)
