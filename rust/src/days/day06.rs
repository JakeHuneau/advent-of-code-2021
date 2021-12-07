#![allow(unused)]
use crate::{Solution, SolutionPair};
use std::fs::read_to_string;

const MAX_AGE: usize = 8;
const RESET_AGE: usize = 6;

pub fn solve() -> SolutionPair {
    let fish_timers: &mut [u128; MAX_AGE + 1] = &mut [0; MAX_AGE + 1];
    read_to_string("../input/day6")
        .unwrap()
        .trim_end()
        .split(',')
        .for_each(|n| fish_timers[n.parse::<usize>().unwrap()] += 1);

    let part_1_solution = get_num_fish(80, fish_timers);
    let part_2_solution = get_num_fish(256 - 80, fish_timers);
    (
        Solution::BigUInt(part_1_solution),
        Solution::BigUInt(part_2_solution),
    )
}

fn get_num_fish(days: u32, fish_timers: &mut [u128; MAX_AGE + 1]) -> u128 {
    for _ in 0..days {
        let fish_deliveries = fish_timers[0];
        for age in 1..=MAX_AGE {
            fish_timers[age - 1] = fish_timers[age];
        }
        fish_timers[RESET_AGE] += fish_deliveries;
        fish_timers[MAX_AGE] = fish_deliveries;
    }
    fish_timers.iter().sum()
}
