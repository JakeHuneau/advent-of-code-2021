#![allow(unused)]
use crate::{Solution, SolutionPair};
use std::fs::read_to_string;

pub fn solve() -> SolutionPair {
    let numbers: Vec<u32> = read_to_string("../input/day1")
        .unwrap()
        .lines()
        .map(|x| x.parse().unwrap())
        .collect();

    let sol1 = get_sol(&numbers, 1);
    let sol2 = get_sol(&numbers, 3);

    (Solution::UInt(sol1), Solution::UInt(sol2))
}

fn get_sol(ls: &[u32], n: usize) -> u64 {
    ls.windows(n + 1).filter(|x| x[n] > x[0]).count() as u64
}
