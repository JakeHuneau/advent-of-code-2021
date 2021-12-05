#![allow(unused)]
use crate::{Solution, SolutionPair};
use std::convert::TryInto;
use std::fs::read_to_string;

// We know this from peaking at data
const NUM_LENGTH: usize = 12;

pub fn solve() -> SolutionPair {
    let bit_arrays: Vec<Vec<u8>> = read_to_string("../input/day3")
        .unwrap()
        .lines()
        .map(|line| {
            let str_numbers = line.split("").collect::<Vec<&str>>();
            str_numbers[1..=NUM_LENGTH]
                .iter()
                .map(|x| x.parse::<u8>().unwrap())
                .collect()
        })
        .collect();

    println!("{:?}", bit_arrays);
    (Solution::Int(1), Solution::Int(1))
}

// fn get_gamma() -> Vec<usize> {

// }
