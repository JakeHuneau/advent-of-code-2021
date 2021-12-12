#![allow(unused)]
use crate::{Solution, SolutionPair};
use std::fs::read_to_string;

struct Point {
    x: isize,
    y: isize,
}

impl Point {
    pub fn new(x: isize, y: isize) -> Self {
        Point { x: x, y: y }
    }
}

pub fn solve() -> SolutionPair {
    let heights: Vec<Vec<u8>> = read_to_string("../input/test")
        .unwrap()
        .lines()
        .map(|line| {
            line.trim_end()
                .chars()
                .into_iter()
                .map(|n| n.to_digit(10).unwrap() as u8)
                .collect()
        })
        .collect();
    let low_points = get_low_points(&heights);
    println!("{:?}", heights);
    let mut part_1: u64 = 0;
    for point in low_points {
        println!(
            "{} {} {}",
            point.y, point.x, heights[point.y as usize][point.x as usize]
        );
        part_1 += (heights[point.y as usize][point.x as usize] + 1) as u64;
    }
    (Solution::UInt(part_1), Solution::UInt(1))
}

fn get_low_points(heights: &Vec<Vec<u8>>) -> Vec<Point> {
    let mut low_points: Vec<Point> = Vec::new();
    for i in 0..heights.len() {
        for j in 0..heights[0].len() {
            let mut low_point = true;
            for neighbor in [
                Point::new((i as isize) - 1, j as isize),
                Point::new((i as isize) + 1, j as isize),
                Point::new(i as isize, (j as isize) - 1),
                Point::new(i as isize, (j as isize) + 1),
            ] {
                if !check_neighbor(heights, &heights[i][j], neighbor.x, neighbor.y) {
                    low_point = false;
                }
                if low_point {
                    low_points.push(Point::new(i as isize, j as isize))
                }
            }
        }
    }
    low_points
}

fn check_neighbor(heights: &Vec<Vec<u8>>, curr_height: &u8, y: isize, x: isize) -> bool {
    if y == -1 || x == -1 {
        return true;
    }
    let neighbor_y = heights.get(y as usize);
    let mut neighbor_y_value: Vec<u8>;
    if neighbor_y == None {
        return true;
    } else {
        neighbor_y_value = neighbor_y.unwrap().to_vec();
    }
    let neighbor = neighbor_y_value.get(x as usize);
    let neighbor_value = neighbor_y_value.get(x as usize);
    if neighbor_value == None {
        return true;
    } else {
        return neighbor_value.unwrap() > curr_height;
    }
}
