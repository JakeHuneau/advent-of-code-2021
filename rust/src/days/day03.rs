#![allow(unused)]
use crate::{util::transpose, Solution, SolutionPair};
use std::convert::TryInto;
use std::fs::read_to_string;

pub fn solve() -> SolutionPair {
    let mut bit_arrays: Vec<Vec<u32>> = read_to_string("../input/day3")
        .unwrap()
        .lines()
        .map(|line| {
            line.trim_end()
                .chars()
                .map(|n| n.to_digit(10).unwrap())
                .collect()
        })
        .collect();

    let bit_counts: String = transpose(bit_arrays.clone())
        .iter()
        .map(|bits| {
            if bits.iter().sum::<u32>() > (bits.len() / 2) as u32 {
                '1'
            } else {
                '0'
            }
        })
        .collect::<Vec<char>>()
        .iter()
        .collect();
    let gamma = u64::from_str_radix(&bit_counts, 2).unwrap();
    let bit_counts_rev: String = bit_counts
        .chars()
        .map(|ch| if ch == '0' { '1' } else { '0' })
        .collect();
    let epsilon = u64::from_str_radix(&bit_counts_rev, 2).unwrap();

    let mut o2_bits: Vec<u8> = Vec::new();
    let mut bit_arrays_co2 = bit_arrays.clone();

    for i in 0..bit_arrays[0].len() {
        let curr_bits = &transpose(bit_arrays.clone())[i];
        let curr_bit_sum = curr_bits.iter().sum::<u32>();
        let curr_bit: u8 = if curr_bit_sum >= curr_bits.len() as u32 - curr_bit_sum {
            1
        } else {
            0
        };
        o2_bits.push(curr_bit);
        bit_arrays = bit_arrays
            .into_iter()
            .filter(|bit_array| bit_array[i] == curr_bit as u32)
            .collect();
    }
    let o2_string: String = o2_bits
        .into_iter()
        .map(|o2_bit| if o2_bit == 1 { '1' } else { '0' })
        .collect::<Vec<char>>()
        .iter()
        .collect();
    let o2 = u64::from_str_radix(&o2_string, 2).unwrap();

    let mut co2_bits: Vec<u8> = Vec::new();
    for i in 0..bit_arrays_co2[0].len() {
        if bit_arrays_co2.len() == 1 {
            co2_bits = bit_arrays_co2[0].clone().into_iter().map(|b| b as u8).collect();
            break;
        }
        let curr_bits = &transpose(bit_arrays_co2.clone())[i];
        let curr_bit_sum = curr_bits.iter().sum::<u32>();
        let curr_bit: u8 = if curr_bit_sum < curr_bits.len() as u32 - curr_bit_sum {
            1
        } else {
            0
        };
        co2_bits.push(curr_bit);
        bit_arrays_co2 = bit_arrays_co2
            .into_iter()
            .filter(|bit_array| bit_array[i] == curr_bit as u32)
            .collect();
    }
    let co2_string: String = co2_bits
        .into_iter()
        .map(|co2_bit| if co2_bit == 1 { '1' } else { '0' })
        .collect::<Vec<char>>()
        .iter()
        .collect();
    let co2 = u64::from_str_radix(&co2_string, 2).unwrap();

    (Solution::UInt(gamma * epsilon), Solution::UInt(o2 * co2))
}
