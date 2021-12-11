#![allow(unused)]
use std::fs::read_to_string;
use std::collections::VecDeque;
use crate::{Solution, SolutionPair};


pub fn solve() -> SolutionPair {
    let mut part_2_scores: Vec<u64> = Vec::new();
    let part_1_tot = read_to_string("../input/day10").unwrap().lines().collect::<Vec<&str>>().iter().map(|line| {
        let mut stack: Vec<char> = Vec::new();
        for bracket in line.chars() {
            match bracket {
                '(' | '{' | '[' | '<' => stack.push(bracket),
                ')' => if stack.pop().unwrap() != '(' {
                        return 3;
                },
                ']' => if stack.pop().unwrap() != '[' {
                    return 57;
                },
                '}' => if stack.pop().unwrap() != '{' {
                    return 1197;
                },
                '>' => if stack.pop().unwrap() != '<' {
                    return 25137;
                },
                _ => unreachable!(),
            }
        };
        part_2_scores.push(get_remaining_stack_points(stack));
        0
    }).sum();

    part_2_scores.sort_unstable();
    (Solution::UInt(part_1_tot), Solution::UInt(part_2_scores[part_2_scores.len() / 2]))
}

fn get_remaining_stack_points(stack: Vec<char>) -> u64 {
    let mut tot: u64 = 0;
    stack.into_iter().rev().for_each(|ch| {
        tot *= 5;
        match ch {
            '(' => tot += 1,
            '[' => tot += 2,
            '{' => tot += 3,
            '<' => tot += 4,
            _ => unreachable!(),
        };
    });
    tot
}