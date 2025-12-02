# Advent of Code 2025

This repository contains solutions for **Advent of Code 2025**, organized by day. Each day has:

* `part1.py` – solution to Part 1
* `part2.py` – solution to Part 2
* `utils.py` – any helper logic shared by parts
* `README.md` – day-specific explanation
* Corresponding input files in the `inputs/` directory

## 📁 Repository Structure

```
advent-of-code-2025/
├── day01/
│   ├── part1.py
│   ├── part2.py
│   ├── utils.py
│   ├── README.md
│   └── __init__.py
├── inputs/
│   └── day01.txt
├── tests/
│   └── test_day01.py
├── README.md          # (this file)
└── .gitignore
```

## ▶️ Running Any Day

Use the Python module runner:

```
python -m dayXX.part1 inputs/dayXX.txt
python -m dayXX.part2 inputs/dayXX.txt
```

Example for Day 01:

```
python -m day01.part1 inputs/day01.txt --start 50
python -m day01.part2 inputs/day01.txt --start 50
```

## 🧪 Running Tests

If using `pytest`:

```
pytest -q
```