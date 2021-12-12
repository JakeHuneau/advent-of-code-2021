#![allow(unused)]
use crate::{Solution, SolutionPair};
use std::cmp;
use std::fs::read_to_string;

pub fn solve() -> SolutionPair {
    let mut crabs: Vec<isize> = read_to_string("../input/day7")
        .unwrap()
        .trim_end()
        .split(',')
        .map(|x| x.parse::<isize>().unwrap())
        .collect::<Vec<isize>>();
    crabs.sort();

    let median_crab = median(&crabs);
    let mean_crab = mean(&crabs);
    let mean_crab_floor = mean_crab as isize;
    let mean_crab_ceil = mean_crab.ceil() as isize;
    let check_ceil = mean_crab_floor != mean_crab_ceil;

    let mut total_fuel_part_1: u64 = 0;
    let mut total_fuel_part_2_floor: u64 = 0;
    let mut total_fuel_part_2_ceil: u64 = 0;

    for crab_location in crabs {
        total_fuel_part_1 += (crab_location - median_crab).abs() as u64;
        total_fuel_part_2_floor += part_2_cost((crab_location - mean_crab_floor).abs());
        if check_ceil {
            total_fuel_part_2_ceil += part_2_cost((crab_location - mean_crab_ceil).abs());
        }
    }

    let mut total_fuel_part_2: u64;
    if check_ceil {
        total_fuel_part_2 = cmp::min(total_fuel_part_2_floor, total_fuel_part_2_ceil);
    } else {
        total_fuel_part_2 = total_fuel_part_2_floor;
    }

    (
        Solution::UInt(total_fuel_part_1),
        Solution::UInt(total_fuel_part_2),
    )
}

fn mean(data: &Vec<isize>) -> f32 {
    (data.iter().sum::<isize>() as f32) / (data.len() as f32)
}

fn median(data: &Vec<isize>) -> isize {
    // Assumes data is sorted
    if data.len() % 2 == 1 {
        // Odd length, take middle value
        data[data.len() / 2]
    } else {
        let middle_index = data.len() / 2;
        (((data[middle_index] as f32) + (data[middle_index - 1] as f32)) / 2.) as isize
    }
}

fn part_2_cost(distance: isize) -> u64 {
    (distance * (distance + 1) / 2) as u64
}
