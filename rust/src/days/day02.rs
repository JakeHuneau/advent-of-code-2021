#![allow(unused)]
use crate::{Solution, SolutionPair};
use std::fs::read_to_string;

pub fn solve() -> SolutionPair {
    let (horizontal, _, depth1, depth2) = read_to_string("../input/day2")
        .unwrap()
        .lines()
        .map(|line| {
            let spl: Vec<&str> = line.split(' ').collect();
            let operation = spl[0];
            let distance: i64 = spl[1].parse().unwrap();
            match operation {
                "forward" => (distance, 0),
                "up" => (0, -distance),
                "down" => (0, distance),
                _ => unreachable!(),
            }
        })
        .fold(
            (0, 0, 0, 0),
            |(horizontal, aim, depth1, depth2), mv| match mv {
                (x, 0) => (horizontal + x, aim, depth1, depth2 + aim * x),
                (0, y) => (horizontal, aim + y, depth1 + y, depth2),
                _ => unreachable!(),
            },
        );

    (
        Solution::Int(horizontal * depth1),
        Solution::Int(horizontal * depth2),
    )
}
