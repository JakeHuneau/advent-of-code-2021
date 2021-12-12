#![allow(unused)]
use crate::{Solution, SolutionPair};
use std::fs::read_to_string;

struct Point {
    x: isize,
    y: isize,
}

impl Point {
    pub fn new(x: isize, y: isize) -> Self {
        Point {
            x: x as isize,
            y: y as isize,
        }
    }
}

struct EnergyLevels {
    energy_levels: Vec<Vec<isize>>,
    flashes: u64,
    rounds: u64,
}

impl EnergyLevels {
    pub fn new(fp: &str) -> Self {
        EnergyLevels {
            energy_levels: read_to_string(fp)
                .unwrap()
                .lines()
                .map(|line| {
                    line.trim_end()
                        .chars()
                        .map(|n| n.to_digit(10).unwrap() as isize)
                        .collect()
                })
                .collect(),
            flashes: 0,
            rounds: 0,
        }
    }

    pub fn step(&mut self) {
        self.rounds += 1;
        let mut need_to_check = true;

        for i in 0..self.energy_levels.len() {
            for j in 0..self.energy_levels[0].len() {
                if self.energy_levels[i][j] < 0 {
                    self.energy_levels[i][j] = 1
                } else {
                    self.energy_levels[i][j] += 1
                }
            }
        }
        while need_to_check {
            need_to_check = false;
            for i_u in 0..self.energy_levels.len() {
                for j_u in 0..self.energy_levels[0].len() {
                    if self.energy_levels[i_u][j_u] > 9 {
                        need_to_check = true;
                        self.flashes += 1;
                        self.energy_levels[i_u][j_u] = isize::MIN; // Get low
                        let i = i_u as isize;
                        let j = j_u as isize;
                        for neighbor in [
                            Point::new(i - 1, j - 1),
                            Point::new(i - 1, j),
                            Point::new(i - 1, j + 1),
                            Point::new(i, j - 1),
                            Point::new(i, j + 1),
                            Point::new(i + 1, j - 1),
                            Point::new(i + 1, j),
                            Point::new(i + 1, j + 1),
                        ] {
                            if neighbor.x < 0
                                || neighbor.y < 0
                                || neighbor.x > (self.energy_levels.len() - 1) as isize
                                || neighbor.y > (self.energy_levels[0].len() - 1) as isize
                            {
                                continue;
                            }
                            self.energy_levels[neighbor.x as usize][neighbor.y as usize] += 1;
                        }
                    }
                }
            }
        }
    }

    pub fn all_flashed(&self) -> bool {
        for i in 0..self.energy_levels.len() {
            for j in 0..self.energy_levels[0].len() {
                if self.energy_levels[i][j] >= 0 {
                    return false;
                }
            }
        }
        true
    }
}

pub fn solve() -> SolutionPair {
    let mut energy_levels = EnergyLevels::new("../input/day11");
    for _ in 0..100 {
        energy_levels.step();
    }
    while !energy_levels.all_flashed() {
        energy_levels.step();
    }

    (
        Solution::UInt(energy_levels.flashes),
        Solution::UInt(energy_levels.rounds),
    )
}
