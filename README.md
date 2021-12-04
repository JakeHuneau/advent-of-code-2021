[Advent of Code 2021](https://adventofcode.com/2021/)

Author: Jake Huneau (jakehuneau@yahoo.com)

# Python

Can run right from command line with python like `python advent_of_code.py <day>` while in `python` directory or build through docker like

```
docker build --tag advent-of-code -f Dockerfile.python .
docker run -e day=<day> advent-of-code:latest
```

If running with python, you will need at least version 3.10 since pattern matching is used.

# Rust
Recomment running with Docker:

```
docker build --tag advent-of-code-rust -f Dockerfile.rust .
docker run -e day=<day> advent-of-code-rust:latest
```