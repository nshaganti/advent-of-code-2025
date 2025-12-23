# Advent of Code 2025 🎄

My solutions for [Advent of Code 2025](https://adventofcode.com/2025) written in Python.

The goal of this repository is to solve the daily puzzles with a focus on **clean code**, **algorithmic efficiency** (Time/Space complexity), and **testability**. Each solution includes integrated unit tests and docstrings explaining the mathematical logic used.

## 📂 Repository Structure

The project is structured to keep solutions self-contained. Each day's script includes the solution logic, complexity analysis, and unit tests.

```text
.
├── inputs/             # Directory for puzzle input files (ignored by git)
│   └── day_01.txt
├── day_01.py           # Solution code with integrated tests
├── day_02.py
├── ...
└── README.md
```

## 🚀 How to Run

1. **Clone the repository:**
```bash
git clone [https://github.com/YOUR_USERNAME/advent-of-code-2025.git](https://github.com/YOUR_USERNAME/advent-of-code-2025.git)
cd advent-of-code-2025

```


2. **Setup Inputs:**
Create an `inputs` folder in the root directory. Download your specific puzzle input from the Advent of Code website and save it as `day_XX.txt`.
```bash
mkdir inputs
# Save your Day 1 input as inputs/day_01.txt

```


3. **Run a Solution:**
Run the python file for the specific day. The script will automatically run unit tests first. If tests pass, it will compute the solution for your input file.
```bash
python day_01.py

```


## 🛠️ Design Philosophy

* **Standard Library Only (Well, mostly!):** Solutions rely on Python's standard library (except for Day 10 which needed numpy & scipy) to reduce external dependencies and complexity.
* **Integrated Testing:** Every file contains a `run_tests()` function that validates logic against the sample data provided in the problem description before attempting the real input.
* **Performance:** Where possible, solutions avoid brute-force simulation in favor of mathematical optimization (e.g., using modular arithmetic instead of iterative loops).

## ⚠️ Note on Inputs

Puzzle inputs are not included in this repository to respect Advent of Code's [copyright and rules](https://adventofcode.com/2025/about). Please log in to the official site to retrieve your unique input data.

---

**Happy Coding!**